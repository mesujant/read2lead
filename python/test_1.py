import os


def fun_test():
	file_name = 'test_1.txt'
	cmd = 'ls -al > {}'.format(file_name)
	a = os.system(cmd)
	with open(file_name, 'r') as f:
		for line in f.readlines():
			print(line)
			#input()
	#print(a)
	pass


if __name__ == '__main__':
	fun_test()