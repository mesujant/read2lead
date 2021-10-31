#find file named test_file_1.txt remove it and print the file name.
# get path, 
# get name of file.



find ./ -type f -name test_file_1.txt -exec rm {} \; -print
