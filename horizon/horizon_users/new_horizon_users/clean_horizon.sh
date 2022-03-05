#AUTHOR`	:	Sujan Tamang <tamang.sujan@worldlink.com.np>	
#DATE		:	शनिवार 22 जनवरी 2022 08:10:18 अपराह्न +0545
#PURPOSE	:	optmize utilization of vmware horizon resources

#find users in multiple pool along with POOL
#find last VM with successful login and delete the other


#find users which is in AD but not in POO and converse
#clean the AD and POOL.

#find users inactive for more than 30 days and make a list of it.
horizon_users3="horizon_users3"
horizon_users_from_pool_1="horizon_users_from_pool_1"
horizon_users="horizon_users"    
horizon_users4="horizon_users4"  
horizon_users_from_pool_2="horizon_users_from_pool_2"
horizon_users2="horizon_users2"
horizon_users_from_pool_0="horizon_users_from_pool_0"
horizon_users_from_pool_3="horizon_users_from_pool_3"

#check user from one file to other and get list of user_to_be_removed_from_fromfile
#users need to be in AD group to access vm,
#users need to remove from pool once they are removed from AD
#
#!/bin/bin/bash
function check_against {
	from_file=$1
	to_file=$2
	echo "checking $from_file against $to_file";read;
	
	while read -r user; do
		if [[ ${#user} > 0 ]];then
			if ! grep -qw $user $to_file ; then
				echo $user >> "remove_from_"$from_file
				
			fi;
		
		fi;
	done < $from_file

}

#check_against  'test11' 'test1'
#read;read;
#echo "checking done"
function AD_vs_POOL {
	if [[ $1 == "horizon_users" ]]; then
		check_against $1 "horizon_users_from_pool_0"

	elif [[ $1 == "horizon_users2" ]]; then
		check_against $1 "horizon_users_from_pool_1"

	elif [[ $1 == "horizon_users3" ]]; then
		check_against $1 "horizon_users_from_pool_2"

	elif [[ $1 == "horizon_users4" ]]; then
		check_against $1 "horizon_users_from_pool_3"
	else
		echo "no matching group"
	fi
}

function POOL_vs_AD {
	if [[ $1 == "horizon_users_from_pool_0" ]]; then
		check_against $1 "horizon_users"
	elif [[ $1 == "horizon_users_from_pool_1" ]]; then
		check_against $1 "horizon_users2"
	elif [[ $1 == "horizon_users_from_pool_2" ]]; then
		check_against $1 "horizon_users2"
	elif [[ $1 == "horizon_users_from_pool_3" ]]; then
		check_against $1 "horizon_users4"
	else
		echo "no matching pool found";
	fi
}

function user_in_multiple_group {
	echo "user in multiple group checking"; read;
	for user in $(cat horizon_users horizon_users2 horizon_users3 horizon_users4 | sort | uniq);do
		echo $user
		match=$(grep -w $user horizon_users horizon_users2 horizon_users3 horizon_users4)
		match_no=$(echo $match | wc -w)
		if [[ $match_no > 2 ]]; then
			echo $match >> "user_in_multiple_group"
		fi
	done
}
function user_in_multiple_pool {
	echo "chcking user in multiple pool"; read;
	for user in $(cat horizon_users_from_pool_0 horizon_users_from_pool_1 horizon_users_from_pool_3 horizon_users_from_pool_4 | sort | uniq);do
		echo $user
		match=$(grep -w $user horizon_users_from_pool_0 horizon_users_from_pool_1 horizon_users_from_pool_2 horizon_users_from_pool_3)
		match_no=$(echo $match | wc -w)
		if [[ $match_no > 2 ]]; then
			echo $match >> "user_in_multiple_pool"
		fi
	done
}


function user_inactive_for_30_days {
	#this need to be taken from logger radius.
	echo "snippet in progress"
}

user_in_multiple_group
user_in_multiple_pool
read;read;
for file in horizon_users3 horizon_users horizon_users4  horizon_users2 ; do 
	echo $file;
	AD_vs_POOL $file;
done;


for file in horizon_users_from_pool_0 horizon_users_from_pool_1 horizon_users_from_pool_2 horizon_users_from_pool_3; do
	POOL_vs_AD  $file;
done;


