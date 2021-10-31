for folder in $(find ./ -type d -name "*")
do 
	echo "$(ls -alt $folder)";
	read;
done

