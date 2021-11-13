#!/usr/bin/bash
nagios_log_path='/home/sujan/scripts'
#date_one_day_ago=$(date '+%m-%d-%Y' -d "1 day ago")

date_yesterday=$(echo $a | awk -F "nagios-" '{print $2}' | awk -F "-00.log" '{print $1}');
date_today=$(date '+%m-%d-%Y');
#date_yesterday=2013-07-15
for file in $(ls $nagios_log_path);
do
	date_yesterday=$(echo $file | awk -F "nagios-" '{print $2}' | awk -F "-00.log" '{print $1}');
	echo $date_yesterday
	read
	if [[ "$date_today" > "$date_yesterday" ]] ;
		then
	    		echo "need to zip ";
		else
			echo "no need to zip";
	fi;
done;

#tar -cvf test_log_II.tar $nagios_log_path/test.log

