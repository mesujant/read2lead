#!/bin/bash

read -p "Enter file name:" file_name
cp $file_name $file_name.bck
name=$(echo $file_name | awk -F "." '{print $1}')
#echo $name
rrdtool dump $file_name $name.xml
sed -i 's/e+1/e+0/g' $name.xml
rm -f $file_name
rrdtool restore $name.xml $file_name