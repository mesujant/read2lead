 

PATH="home/sujan/Documents/read2lead/horizon/horizon_users/"

# for file1 in $(ls $PATH);
# do
# 	for file2 in $(ls $PATH);
# 	do 
# 		if [[ $file1 != $file2 ]];
# 		then
# 			echo $file1 $file2;
# 		fi
# 	done;
# done;

for file1 in $(ls $PATH);  do for file2 in $(ls $PATH); do if [[ $file1 != $file2 ]];then echo $file1 $file2; fi;done;done;