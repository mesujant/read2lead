import os
import time


#checkk if all directories are included with its absoluted path:
def check_if_all_directories_serialized(directories):
	for directory in directories:
		if isinstance(directory, list):
			print(directory)
			return False
	return True

def get_latest_modified_time(path):
	#files = [r+"/"+d1+"/"+f1 for r, d, f in os.walk(path) for d1 in d for f1 in f]

	#list all directories from the given path:
	directories = [r+"/"+d1+"/" for r, d, f in os.walk(path) for d1 in d]
	
	#checkk if all directories are included with its absoluted path:
	if not check_if_all_directories_serialized(directories):
		print("directories list not compatible")
		input()
	# else:
	# 	print("OKAY")

	if check_if_all_directories_serialized(directories):

		for i, directory in enumerate(directories):
			if directory.find("//") != -1:
				directory = directory.replace("//", "/")
				directories[i] = directory

	 
	latest_modified_time = 0
	latest_modified_file = ''
	for directory in directories:
		 
		list_of_files = [directory + file for file in os.listdir(directory)]

		if len(list_of_files) > 0: 
			latest_file = max(list_of_files, key=os.path.getctime)
			print(latest_file)
			print(latest_file.split('/')[-1] , time.ctime(os.path.getctime(latest_file)))

			if os.path.getctime(latest_file) > latest_modified_time:
				latest_modified_time = os.path.getctime(latest_file)
				latest_modified_file = latest_file


	print("*************************************************************************\n")
	print("Latest modified file:", latest_modified_file)
	print("Latest modified time:", time.ctime(latest_modified_time))
	print("\n***********************************************************************\n")