#/bin/python3

import time
import hashlib

def main():
	
	# Get first user of file
	file1 = open('users', 'r')
	Lines1 = file1.readlines()
	first_user = Lines1[1]
	login_info = first_user.split(',') # [0] = usr, [1] = hashed pswd
	
	# Get rid of those sneaky little new lines
	login_info[1] = login_info[1].strip()

	# Get dictionary
	file2 = open('password_dictionary', 'r')
	Lines2 = file2.readlines()

	start = time.time()

	print("Cracking password for user: " + login_info[0])
	print(login_info[0] + "'s hash is: " + login_info[1])
	# Main loop
	for line in Lines2:
		try:
			h = hashlib.sha256(bytes(line, 'UTF-8').strip())
			if h.hexdigest() == login_info[1]:
				print("Password is: " + line)
				break
		except:
			pass

	end = time.time()
	file1.close()
	file2.close()
	print("Total elapsed time: " + str(end - start))

if __name__ == "__main__":
	main()
