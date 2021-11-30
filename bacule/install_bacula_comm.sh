#!/bin/bash

# Enter the desired version
bacula_version="11.0.5"

# Enter the key received by email
bacula_key="60fe7dca2d10e"


# Requirements to install Bacula by packages
yum install -y zip wget bzip2


# Download the repository keys
wget -c https://www.bacula.org/downloads/Bacula-4096-Distribution-Verification-key.asc -O /tmp/Bacula-4096-Distribution-Verification-key.asc


# Add key in the local repository
rpm --import /tmp/Bacula-4096-Distribution-Verification-key.asc


# Create the Bacula Community repository
echo "[Bacula-Community]
name=CentOS - Bacula - Community
baseurl=http://www.bacula.org/packages/${bacula_key}/rpms/${bacula_version}/el7/
enabled=1
protect=0
gpgcheck=0" > /etc/yum.repos.d/bacula-community.repo



#==================================================================
# Install PostgreSQL
yum install -y postgresql-server
yum install -y bacula-postgresql --exclude=bacula-mysql
postgresql-setup initdb


# Enable and start PostgreSQL during boot
systemctl enable postgresql
systemctl start postgresql


# Create the Bacula database with PostgreSQL
su - postgres -c "/opt/bacula/scripts/create_postgresql_database"
su - postgres -c "/opt/bacula/scripts/make_postgresql_tables"
su - postgres -c "/opt/bacula/scripts/grant_postgresql_privileges"
###################################################################

usermod -aG tape bacula
usermod -aG disk bacula
# Disables selinux:
setenforce 0
sudo sed -i "s/enforcing/disabled/g" /etc/selinux/config
# Firewall Rules
firewall-cmd --permanent --zone=public --add-port=9101-9103/tcp
firewall-cmd --reload
# Enable the start of daemons during boot
systemctl enable bacula-fd.service
systemctl enable bacula-sd.service
systemctl enable bacula-dir.service


# Start the Bacula daemons
systemctl start bacula-fd.service
systemctl start bacula-sd.service
systemctl start bacula-dir.service


# Create shortcut in /usr/sbin with Bacula binaries
# This allows you to run the daemons and utilities
# Without entering the /opt/bacula/bin directory
for i in `ls /opt/bacula/bin`; do
    ln -s /opt/bacula/bin/$i /usr/sbin/$i;
done


# Replace the bconsole.conf address to localhost by default
sed '/[Aa]ddress/s/=\s.*/= localhost/g' -i /opt/bacula/etc/bconsole.conf


