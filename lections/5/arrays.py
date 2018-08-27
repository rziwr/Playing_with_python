#!/usr/bin/python


A = [1, 2, 3, 4, 5]
for x in A:
	print (x, type (x))
	x += 1
	print (x)
print (A)

for k in range (5):
	A[k] = A[k] * A[k]


#A = [0]*1000
C = A
C [0] = 100
print (A[0])
