
import os
import shutil as s

#edit bacula client
#set director name to bacula-dir
#set director-mon to bacula-mon
# set for bacula to connet to clinet to host-address
# set File Daemon running address to its FQDN rather than localhost.

def edit_bacula_client():
	 
	lines = []
	with open('bacula-fd.conf', 'r') as f:
		lines = f.readlines()

	for i, line in enumerate(lines):
		if "Director {" in line:
			j=i
			while "}" not in lines[j]:
				if "Name" in lines[j]:
					print(lines[j].replace(os.uname().nodename, 'bacula'))
				if "Password" in lines[j]:
					temp = lines[j].split("=")
					temp[1] = ' "'+ os.uname().nodename + '"\n'
					print("=".join(temp))
					lines[j] = "=".join(temp)

				j += 1
			#input()

		if 'FileDaemon {' in line:
			lines_0_i = lines[:i+1]
			lines_i_ = lines[i+1:]
			FDAddress = "  FDAddress = " + os.uname().nodename + "\n"
			lines_0_i.append(FDAddress)
			lines =  lines_0_i + lines_i_
			 
	s.copy('bacula-fd.conf', 'bacula-fd.conf.bck')

	 
	with open('bacula-fd.conf', 'w') as f:
		for line in lines:
			f.write(line)


if __name__ == '__main__':
	edit_bacula_client()
