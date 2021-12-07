import os
import shutil as s

def read_file(file_path):
	with open(file_path, 'r') as f: return f.readlines()


def find_content_of_section(lines, section):
	open_brac_count = 0
	close_brac_count = 0
	contents = []
	for i, line in enumerate(lines):
		if section in line and "{" in line:
			#print(line)
			

			for j in range(i, len(lines)):

				if "{" in lines[j]:
					open_brac_count += 1
				 
				contents.append(lines[j])
				if "}" in lines[j]:
					close_brac_count += 1
				if open_brac_count == close_brac_count:
					break
	return contents		

def create_new_dir_conf(contents_modulated, file):
	contents = []
	content_config = []
	with open(file, 'r') as f:
		contents =  f.readlines()

	for content in contents:
		if content not in contents_modulated:
			content_config.append(content)


	with open('new_director.conf', 'w') as f:
		for content in content_config:
			f.write(content)


def create_section_files():
	contents_modulated = []
	file_path = os.getcwd() + "/" + "bacula-dir.txt"
	lines = read_file(file_path)
	 
	sections = ['Client', 'Pool', 'Storage', 'Job', 'Schedule', 'Autochanger', 'FileSet', 'Director', 'Messages', 'Console', 'Catalog', ]
	for section in sections:
		# print(section)
		# input()
		contents = find_content_of_section(lines, section)
		contents_modulated += contents
		with open(section+"s.conf", 'w') as f:
			for content in contents:
				f.write(content)

	f0 = open('Directors_test.conf', 'a')

	for section in ['Director', 'Messages', 'Console', 'Catalog']:
		with open(section+"s.conf", 'r') as f:
			for line in f.readlines():
				f0.write(line)

		os.remove(section+"s.conf")

	if not os.path.isdir(os.getcwd()+"/config.d"):
		os.mkdir(os.getcwd()+"/config.d")

	# for section in sections:
	# 	if section not in ['Director', 'Messages', 'Console', 'Catalog']:
	# 		s.move(os.getcwd() + "/" + section + "s.conf", os.getcwd() + '/config.d/')
	 


	f0.write("@/opt/bacula/etc/config.d/Autochangers.conf")
	f0.write("\n@/opt/bacula/etc/config.d/Clients.conf")
	f0.write("\n@/opt/bacula/etc/config.d/Jobs.conf")
	f0.write("\n@/opt/bacula/etc/config.d/FileSets.conf")
	f0.write("\n@/opt/bacula/etc/config.d/Schedules.conf")
	f0.write("\n@/opt/bacula/etc/config.d/Pools.conf")

	f0.close()


if __name__ == '__main__':
	create_section_files()

	