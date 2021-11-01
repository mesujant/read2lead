#check for exception
#run as cron tab:

import requests

conn_timeout = 2
read_timeout = 60
timeouts = (conn_timeout, read_timeout)
r = requests.get('https://onlineedlreg.dotm.gov.np/', timeout=timeouts)

if r.ok:
	print("found")
else:
	print("not found")