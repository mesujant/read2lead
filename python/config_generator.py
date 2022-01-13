

def client_config(client_name):



def job_config(client_name):
	#find all jobdefs
	#crawl all info needed for job defs.
	#job config based on job def

	job_config = "Job {
  Name = "CLIENT_NAME"
  Type = Backup
  Level = Incremental
  Client = CLIENT_NAME
  FileSet = "FILE_SET" # predefined set
  Schedule = "WeeklyCycle"
  Storage = File2
  Messages = Standard
  Pool = File
  SpoolAttributes = yes
  Priority = 10
  Write Bootstrap = "/opt/bacula/working/%c.bsr"

}"
	pass


def 