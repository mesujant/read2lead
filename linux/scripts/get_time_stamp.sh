#/usr/bin/bash

for i in `ls` 
    do
      echo `ls -l $i` > test_output.txt;
      awk '{print "filename:", $9, $6, $7, $8}' test_output.txt;
    done
