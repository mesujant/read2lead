import os

def read_file(file_path):
	with open(file_path, 'r') as f: return f.readlines()


def find_content_of_section(lines, section):
	open_brac_count = 0
	close_brac_count = 0
	contents = []
	for i, line in enumerate(lines):
		if section in line and "{" in line:
			#print(line)
			open_brac_count += 1

			for j in range(i, len(lines)):
				 
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

	f0.write("@ | find etc/bacula /config.d -type f -name *.conf -exec @{} \;")
 
     

		 


if __name__ == '__main__':
	create_section_files()

	