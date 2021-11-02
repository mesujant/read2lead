#check for exception
#run as cron tab:

import requests

def check_availability(url):
	conn_timeout = 2
	read_timeout = 60
	timeouts = (conn_timeout, read_timeout)
	r = requests.get(url, timeout=timeouts)
	return r.ok

def send_notification():
	pass

if __name__ == '__main__':
	url = 'https://onlineedlreg.dotm.gov.np/'
	#print(check_availability(url))
	 
	while not check_availability(url):
		print("page not found:")

	send_notification()


 