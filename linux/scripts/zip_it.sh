#!/usr/bin/bash
NAGIOS_LOG_PATH="/home/sujan/scripts/"
#echo $NAGIOS_LOG_PATH;

for file in $(ls $NAGIOS_LOG_PATH);
do
	#if [[ $file != *"tar"* ]];
	if [[ $file != *"tcp"* ]]; 
	then
		ZIP_FILENAME="$NAGIOS_LOG_PATH$file.tar.gz"
		echo $file "need to zip"
		tar -zcfv $ZIP_FILENAME $NAGIOS_LOG_PATH$file
	fi
done;