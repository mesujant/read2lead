import pdb
class Student:
	def __init__(self, std):
		self.count = std

	def print_std(self):
		for i in range(self.count):
			pdb.set_trace()
			print(i)
		return

def debug_test():
	n = 1
	print("0")
	pdb.set_trace()
	n += 1
	n += 1
	print("1")
	print("2")
	print("3")

if __name__ == '__main__':
	debug_test()
	Student(5).print_std()