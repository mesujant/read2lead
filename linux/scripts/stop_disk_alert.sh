#!/usr/bin/bash
HOME="/home/sujan/Desktop/test"
RECORDING="/var/spool/asterisk/monitor/"
SQLFILES="/usr/admin/scripts/rsyncBackup/mysql/"
LOGFILES="/var/log/asterisk/"


FILE0=$(date +%m --date="today")
FILE1=$(date +%m --date="1 month ago")
FILE2=$(date +%m --date="2 month ago")
FILE3=$(date +%m --date="3 month ago")
RECORD_YEARS=$(ls $RECORDING)
echo $RECORD_YEARS
read
for record in $(ls $RECORDING$RECORD_YEARS)
do
      echo "files to be deleted"
      if [[ $record != $FILE0 && $record != $FILE1 && $record != $FILE2 && $record != $FILE3 ]]
      then
              echo $record
      fi

#done;
#read
SFILE1=$(date +%Y-%m-%d --date="today")
SFILE2=$(date +%Y-%m-%d --date="1 day ago")
SFILE3=$(date +%Y-%m-%d --date="1 week ago")

#echo $SFILE1
#echo $SFILE2
#echo $SFILE3
read
#echo "sql files : $(ls $SQLFILES) "
for sql_file in $(ls $SQLFILES | grep -i .tar.gz)
do 
      date_sql=$(echo $sql_file | cut -d"." -f1 | cut -d"-" -f3,4,5)
      if [[ $date_sql == $SFILE1 || $date_sql == $SFILE2 || $date_sql == $SFILE3 ]]
      then
              echo "$sql_file file matched"
      else
              #remove file here
              echo "$sql_file dont matched"
done
#read

#echo "log files: $(ls $LOGFILES)"

FILES=$(ls -ltu $HOME$LOGFILES | grep -i full | head -5 | awk -F" " '{print $9}')

echo $FILES
read

for file in $(ls -a $HOME$LOGFILES | grep -i full );
do
        if [[ " ${FILES[*]} " =~ "${file}" ]]
        then
                echo "$file to kept"
        else
                #remove files here;
                echo "$file to removed"
        fi

done
read