#/usr/bin/bash

#find latest modified file of the directory
#now the question is to traverse through the directories and find the latest modified file 
#echo $(ls -alt | head -2 | tail -1) | awk '{print $6, $7, $8}'

for i in `ls` 
    do
      echo `ls -l $i` > test_output.txt;
      awk '{print "filename:", $9, $6, $7, $8}' test_output.txt;
    done
