
import os

def remove_spikes(file_paths):
	for file in file_paths:
		copy_cmd = "cp {} /home/sujan.tmg/backups/".format(file)
		os.system(copy_cmd)
		raw_input()
	#backup file
	#check all  backups
	#dump 
	#remove all spikes 
	#check, re-check
	#remove old rrd file 
	#restore rrd file

	pass


if __name__ == '__main__':
	file_name = "test_file.txt"
	temp = []
	file_paths = []
	with open(file_name, 'r') as f:
		temp = f.readlines()
	
	# print(file_paths[0])
	# rrd_file = (file_paths[0].split(":")[1])
	# print(rrd_file.split("=")[1])

	for line in temp:
		rrd_file = (line.split(":")[1])
		file_path = (rrd_file.split("=")[1])
		print(file_path)
		# raw_input()
		file_paths.append(file_path)
	print(len(set(file_paths)))

	print(len(file_paths))

	# for line in file_paths:
	# 	print(line)
	# 	raw_input()

