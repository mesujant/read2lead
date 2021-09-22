import os
import time

#path = "/home/sujan/Documents/read2lead"


def git_upload_files(path):
	os.chdir(path)
	msg0 = '"'
	msg = time.ctime(time.time()) + "commit"
	git_add = "git add *"
	git_commit = "git commit -m {}{}{}".format(msg0, msg, msg0)
	git_push = "git push origin main"
	
	os.system(git_add)
	os.system(git_commit)
	os.system(git_push)
	#print(os.listdir(os.getcwd()))


if __name__ == '__main__':
	path = "/home/sujan/Documents/read2lead"
	git_upload_files(path)


