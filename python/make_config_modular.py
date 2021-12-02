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
			#while close_brac_count != open_brac_count:
			for j in range(i, len(lines)):
				print(lines[j])
				contents.append(lines[j])
				if "}" in lines[j]:
					close_brac_count += 1
				if open_brac_count == close_brac_count:
					break
	return contents		


def create_section_files():
	file_path = os.getcwd() + "/" + "bacula-dir.txt"
	lines = read_file(file_path)

	sections = ['Client', 'Pool', 'Storage', 'Job', 'Schedule', 'Autochanger']
	for section in sections:
		print(section)
		contents = find_content_of_section(lines, section)
		with open(section+"s.conf", 'w') as f:
			for content in contents:
				f.write(content)
		input()

		 


if __name__ == '__main__':
	create_section_files()

	# file_path = os.getcwd() + "/" + "bacula-dir.txt"
	# lines = read_file(file_path)
	# sections = ['Client', 'Pool', 'Storage', 'Job', 'Schedule', '']
	# for section in sections:
	# 	print(section)
	# 	find_content_of_section(lines, section)
	# 	input()
	#  