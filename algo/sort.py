#!/usr/bin/env python

def insert_sort (A):
	""" Sort of list A by insertion sort """
	n = len(A)
	for top in range (1, n):
		k = top
		while k > 0 and A[k-1] > A[k]:
			A[k], A[k-1] = A[k-1], A[k]
			k -= 1
	pass


def choise_sort (A):
	""" Sort of list by choise sort """
	n = len (A)
	for pos in range (0, n-1):
		for k in range(pos+1, n):
			if A[k] < A[pos]:
				A[k], A[pos] = A[pos], A[k]

def bubble_sort(A):
	""" Sort list by buuble method """
	n = len(A)
	for bypass in range(1, n):
		for k in range(0, n-bypass):
			if A[k] > A[k+1]:
				A[k], A[k+1] = A[k+1], A[k]

def test_sort (sort_algorithm):
	print (sort_algorithm.__doc__)
	print ("testcase 1: ")
	A = [4, 2, 5, 1, 3]
	A_sorted = [1, 2, 3, 4, 5]
	sort_algorithm(A) 
	print ("Ok" if A == A_sorted else "False")

	print ("testcase 2: ")
	A = list(range(10, 20)) + list(range (0, 10))
	A_sorted = list (range (0, 20))
	sort_algorithm(A) 
	print ("Ok" if A == A_sorted else "False")
	
	print ("testcase 3: ")
	A = [4, 2, 5, 2, 1]
	A_sorted = [1, 2, 2, 4, 5]
	sort_algorithm(A) 
	print ("Ok" if A == A_sorted else "False")




if __name__ == "__main__":
	test_sort(insert_sort)
	test_sort(choise_sort)
	test_sort(bubble_sort)
