#/bin/python3

import time
import hashlib

def main():
	
	# Get first user of file
	file1 = open('users', 'r')
	Lines1 = file1.readlines()
	
	# Get dictionary
	file2 = open('password_dictionary', 'r')
	Lines2 = file2.readlines()

	# Dictionary to hold key-value pairs
	# key = hash # value = pass
	my_dict = dict()

	start = time.time()

	# Add password_dictionary to python dictionary
	for line in Lines2:
		h = hashlib.sha256(bytes(line, 'UTF-8').strip())
		my_dict[h.hexdigest()]=line

	# Main loop
	# skip first line
	for line in Lines1[1:]:
		user = line
		login_info = user.split(',')
		login_info[1] = login_info[1].strip()
		print("Cracking password for user: " + login_info[0])
		print(login_info[0] + "'s hash is: " + login_info[1])

		password = my_dict.get(login_info[1])
		#key_lookup = list(mydict.keys())[list(mydict.values()).index(password)]
		print("Password is: " + password)
	
	end = time.time()
	file1.close()
	file2.close()
	print("Total elapsed time: " + str(end - start))

if __name__ == "__main__":
	main()
