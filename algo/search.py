#!/usr/bin/env python3

def search (str, find):
	f_len = len (find)
	f_ind = 0
	res = -1
	for i in range (len(str)):
		if str[i] == find[f_ind]:
			if f_ind == 0:
				res = i
			f_ind += 1
			if f_ind == f_len:
				return res
		else:
			f_ind = 0
			res = -1
	return res

def test (a1, a2, res):
	print (str(a2), " : ", end = '')
	if search (a1, a2) == res:
		print ("OK")
	else:
		print ("Fail")


A = "Many any easy busy"

test_data = [
	[[A, "Many"], 0],
	[[A, "any"], 1],
	[[A, "145"], -1]]

def test_all ():
	global test_data
	
	for i in range(len(test_data)):
		[a, b], c = test_data[i]
		test (a, b, c)

if __name__ == "__main__":
	A = "Many 123 345 "
	#print (int(search (A, "233")))
	#test (A, "any", 1)
	#test (A, "Man", 0)
	#test (A, "145", -1)
	
	test_all()
