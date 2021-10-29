import os
import time


def get_latest_modified_time(path):
	files = [r+"/"+d1+"/"+f1 for r, d, f in os.walk(path) for d1 in d for f1 in f]
	directories = [r+"/"+d1+"/" for r, d, f in os.walk(path) for d1 in d]
	directories_filtered = []
	for directory in directories:
		if directory.find("//") != -1:
			directory.replace("//", "/")
		directories_filtered.append(directory)

	print("completed:")
	input()
	filter_directories = []
	for i, directory in enumerate(directories_filtered):

		if directory.find(' ') != -1:
			print(i, directory)
			temp = directory.split('/')

 
			for j, value in enumerate(temp):
				if value.find(" ") != -1:
					temp[j] = "'" + value + "'"
			directories[i] = "/".join(temp)
		 

	 
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


	print("*************************************************************************\n")
	print("Latest modified file:", latest_modified_file)
	print("Latest modified time:", time.ctime(latest_modified_time))
	print("\n***********************************************************************\n")

