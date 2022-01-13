import os


def registered_hosts():
	r_hosts = []
	with open('Clients.conf', 'r') as f:
		r_hosts = f.readlines()
	r_hosts = [line.strip().split("=")[1] for line in r_hosts if "Name" in line and "#" not in line]
	return [host.lstrip() for host in r_hosts]


def obtained_hosts():
	o_hosts = []
	with open('hosts', 'r') as f:
		o_hosts = f.readlines()
	#ignoring if anything starts with #
	o_hosts = [line.strip().split("	")[0] for line in o_hosts if "[" not in line and len(line) > 2 and "#" not in line]
	#print(o_hosts)
	return o_hosts

def unregistered_hosts():
	director = "172.28.255.16"
	r_hosts = registered_hosts()
	u_hosts = []
	o_hosts = obtained_hosts()
	 
	for o_host in o_hosts:
		if o_host not in r_hosts and o_host != director:
			u_hosts.append(o_host)
		# else:
		# 	print(o_host, "already registed ")
	print(u_hosts)
	with open('unregistered_hosts.txt', 'w') as f:
		for u_host in u_hosts:
			f.write(u_host + "\n")


if __name__ == '__main__':

	unregistered_hosts()


