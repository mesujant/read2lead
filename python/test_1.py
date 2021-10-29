import os
import time

# def get_directories(path="/"):
# 	dir_file_name = path +'dirs2.txt'
# 	cmd = 'find {} -type d -name "*" > {}'.format(path, dir_file_name)	 
# 	os.system(cmd)
# 	directories = []
# 	with open(dir_file_name, 'r') as f:
# 		directories = f.readlines()
# 	#print(directories)
# 	#input()
# 	for value in directories:
# 		print(value)
		
# 	return directories

# def get_files(path='/'):
# 	files_file_name = path +'files.txt'
# 	cmd = 'find {} -type f -name "*" > {}'.format(path, files_file_name)	 
# 	os.system(cmd)
# 	files = []
# 	with open(files_file_name, 'r') as f:
# 		files = f.readlines()
# 	print(files)
# 	input()

#find the depth of the directories:

# def get_latest_modified_time(path):
# 	directories = get_directories(path)
# 	for directory in directories:
# 		i = 0
# 		while i != len(directory):
# 			print(directory)
# 			i += 1
# 			input()

# 		#print(len(directory), "\n", directory)
# 		input()


# def fun_test():
# 	file_name = 'test_1.txt'
# 	cmd = 'ls -al > {}'.format(file_name)
# 	a = os.system(cmd)
# 	with open(file_name, 'r') as f:
# 		for line in f.readlines():
# 			print(line)
# 			#input()
# 	#print(a)
# 	pass

#solve issue of folder name with spaces:

def fun_test(path):
	files = [r+"/"+d1+"/"+f1 for r, d, f in os.walk(path) for d1 in d for f1 in f]
	directories = [r+"/"+d1+"/" for r, d, f in os.walk(path) for d1 in d]
	# directories_filtered = [directory.replace("//", "/") for directory in directories if directory.find("//") != -1]
	directories_filtered = []
	for directory in directories:
		if directory.find("//") != -1:
			directory.replace("//", "/")
		directories_filtered.append(directory)

	print("completed:")
	input()
	filter_directories = []
	for i, directory in enumerate(directories_filtered):
		#check if all directories have been serialized:
		# if len(directory) > 1:
		# 	print("length of directory greater than one:")
		# 	print(directory)
		# 	input()
		# if directory.find("//") != -1:
		# 	directory.replace("//", "/")
		# 	print(directory)


		if directory.find(' ') != -1:
			print(i, directory)
			temp = directory.split('/')

		#print(directory)
			for j, value in enumerate(temp):
				if value.find(" ") != -1:
					temp[j] = "'" + value + "'"
			directories[i] = "/".join(temp)
			#print(directories[i])
			#input()
		#input()

	#find the latest file:
	latest_modified_time = 0
	latest_modified_file = ''
	for directory in directories_filtered:
		 
		list_of_files = [directory + file for file in os.listdir(directory)]

		if len(list_of_files) > 0: 
			latest_file = max(list_of_files, key=os.path.getctime)
			print(latest_file)
			print(latest_file.split('/')[-1] , time.ctime(os.path.getctime(latest_file)))

			if os.path.getctime(latest_file) > latest_modified_time:
				latest_modified_time = os.path.getctime(latest_file)
				latest_modified_file = latest_file


	print("***********************************************\n")
	print("Latest modified file:", latest_modified_file)
	print("Latest modified time:", latest_modified_time)
	print("***********************************************\n")
			 
if __name__ == '__main__':
	#fun_test()
	path = "/home/sujan/Documents/read2lead/"
	#get_directories(path)
	#get_files(path)
	#get_latest_modified_time(path)
	fun_test(path)

