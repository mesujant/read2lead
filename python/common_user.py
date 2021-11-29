import os

user_file_path = "/home/sujan/Documents/read2lead/horizon/horizon_users/"
 

def read_file(file):
	users = []
	with open(file, 'r') as f:
		users = f.readlines()
	return [user.strip() for user in users if len(user) > 2]

def get_total_user_count(all_users):
	unique_users = []
	for pool, users in all_users:
		unique_users += users
	return len(set(unique_users)), set(unique_users)


def get_user_associated_pool(total_users, all_users):
	user_pool = []
	for user in total_users:
		pools = []
		for pool, users in all_users:
			if user in users:
				pools.append(pool)
		user_pool.append([user, pools])
	return (user_pool)

def display_result(user_pools):
	one_pool_user = 0
	two_pool_user = 0
	three_pool_user = 0
	four_pool_user = 0

	print("\n##########################################\n")
	for user, pool in user_pools:
		if len(pool) == 1:
			print(user, pool)
			one_pool_user += 1
	
	print("\n##########################################\n")
	print("Total one Pool User :", one_pool_user)
	print("\n##########################################\n")
	print("\n##########################################\n")
	for user, pool in user_pools:
		if len(pool) == 2:
			print(user, pool)
			two_pool_user += 1

	print("\n##########################################\n")
	print("Total two Pool User :", two_pool_user)
	print("\n##########################################\n")
	print("\n##########################################\n")

	for user, pool in user_pools:
		if len(pool) == 3:
			print(user, pool)
			three_pool_user += 1
	print("\n##########################################\n")
	print("Total three Pool User :", three_pool_user)
	print("\n##########################################\n")
	print("\n##########################################\n")

	for user, pool in user_pools:
		if len(pool) == 4:
			print(user, pool)
			four_pool_user += 1
	print("\n##########################################\n")
	print("Total four Pool User :", four_pool_user)
	print("\n##########################################\n")
	print("\n##########################################\n")

def notify_if_multiple_pool_assigned():
	#send mail with username and desktop pool
	pass


def get_report(all_users):

	total_horizon_users, all_horizon_users = get_total_user_count(all_users)
	#print(total_horizon_users, all_horizon_users)
	user_pools = get_user_associated_pool(all_horizon_users, all_users)
	display_result(user_pools)


def read_file(user_file_path):
	all_users = []
	for file in os.listdir(user_file_path):
		all_users.append([file, read_file(user_file_path+file)])

	get_report(all_users)


if __name__ == "__main__":
	all_users = []
	for file in os.listdir(user_file_path):
		all_users.append([file, read_file(user_file_path+file)])
	

	get_report(all_users)