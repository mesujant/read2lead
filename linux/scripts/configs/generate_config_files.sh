#create job def as according to the host
# create file set
# create pool
# create autochangers
# create schedules.
# extensive care should be given to concurrent jobs.

function client_config {
	echo '
	Client {
	  Name = '$1'
	  Address = '$1'
	  FDPort = 9102
	  Catalog = MyCatalog
	 # Password = "OQCMipCPmdosElU9DDWf5aOo4gynkMg227AAZ2c6oOEJ"          # password for FileDaemon
	  Password = "'$1'"
	  File Retention = 60 days            # 60 days
	  Job Retention = 6 months            # six months
	  AutoPrune = yes                     # Prune expired Jobs/Files
	  Maximum Concurrent Jobs = 10
	} ' 
 

}


function fileset_config {

	echo "testing";

}

function schedule_config {
	echo "testing";

}

function pool_config {
	echo "testing";

}

function autochanger_config {
	echo "testing";

}



function job_config {
	#find if any matching job defs
	#what if no matching job defs found,
		# need to find everything from Clients, filesets, schedules,
		# pools, autochangers.

	jobDef=""
	jobDefs=$(grep -A 2 "JobDefs {" /home/sujan/Documents/read2lead/linux/scripts/configs/Job | grep "Name" | cut -d"=" -f2)
	
	# if found in job def
	# if not found in job def
	for jobdef in ${jobDefs};
	do
		if echo "$jobdef" | grep -iq "$1";
		then
			#echo "$jobdef job def found";
			jobDef=$jobdef
			echo '
				Job {
				  Name = "'$1'"
				  JobDefs = '$jobDef'
				  Client = '$1'
				}
			' 
			client_config $1
			break
		 
		fi
	done

	if [[ ${#jobDef} == 0 ]]
	then
		#here i have call all the functions;
		echo "no job def matched"
	fi

 

}

# echo "Enter client name:";
# read CLIENT_NAME;
#echo $client_name;

job_config $1

