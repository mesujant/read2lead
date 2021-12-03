#!/usr/bin/bash

 

cd /home/sujan/Documents/read2lead/horizon/horizon_users/

while read -r inactive_user
do
	if grep -q $inactive_user users_in_multiple_pool.txt
	then
		echo $inactive_user >> first_step_removal.txt
	else
		echo $inactive_user "is not assigned multiple pool"
	fi


done < inactive_user_for_30_days.txt