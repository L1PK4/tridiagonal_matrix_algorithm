#!usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

def holets(A):
	x = A[0, 0]
	b = np.mat(A[1:, 0])
	B = A[1:, 1:]
	return B - (b.T * b) / x

def L(A):
	n = A.shape[0]
	if n == 0:
		return np.sqrt(A)
	b = np.mat(A[1:, 0])
	x = np.sqrt(A[0, 0])
	print(np.mat(x), np.zeros((1, n - 1)), b.T / x)
	return np.bmat([[np.mat(x), np.zeros((1, n - 1))], [b.T / x, L(holets(A))]])


def main():
	n = int(input("Enter n: "))
	print("Enter {0}x{0} matrix:".format(n))
	a = np.array([list(map(float, input().split(maxsplit=n))) for i in range(n)])
	print(a)
	print(L(a))

if __name__ == '__main__':
	main()