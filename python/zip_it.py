import os 
#from datetime import datetime as dt
#write test case for it
#check for file size greater than 1G: if remove takes place before zipping
#

if __name__ == '__main__':
	#path = "/home/sujan/Documents/read2lead/python/archives/"
	path = "/home/sujan/scripts/"
	files = os.listdir(path)
	
	for file in files:
		if ".log" in file and ".tar" not in file:
			full_file_path = path+file
			target_file_path = path + file + ".tar.gz"
			cmd_zip = 'tar -zcvf {} {}'.format(target_file_path, full_file_path)
			cmd_remove = 'rm -f {}'.format(path+file)
			print("file zipped:")
			os.system(cmd_zip)
			os.system(cmd_remove)

	
	 



