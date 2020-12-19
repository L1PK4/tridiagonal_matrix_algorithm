import numpy as np

def algo(a, b, c, d):
	'''
	Tridiagonal algorithm
	|	b1 	c1 	0 	0	|	d1	|
	|	a1 	b2 	c2 	0	|	d2	|
	|	0	a2	b3	c3	|	d3	|
	|	0	0	a3	b4	|	d4	|
	->
	|	x1	x2	x3	x4	|
	'''

	nf = len(d) # number of equations
	ac, bc, cc, dc = tuple(map(np.array, (a, b, c, d))) # copy arrays
	for it in range(1, nf):
		mc = ac[it - 1] / bc[it - 1]
		bc[it] = bc[it] - mc * cc[it - 1] 
		dc[it] = dc[it] - mc * dc[it - 1]

	xc = bc
	xc[-1] = dc[-1]/bc[-1]

	for il in range(nf-2, -1, -1):
		xc[il] = (dc[il]-cc[il]*xc[il+1])/bc[il]

	return xc

def matrix_to_3list(arr):
	'''
	Convert matrix to 3 vectors:

	Arr -> 
	|	b1 	c1 	0 	0	|
	|	a1 	b2 	c2 	0	|
	|	0	a2	b3	c3	|
	|	0	0	a3	b4	|
	'''
	m, n = np.shape(arr)
	# if np.linalg.det(arr) == 0:
	# 	return -1
	if m != n:
		print('m != n')
		return -1
	for i in range(n):
		for j in range(n):
			if (i == j) or (i - 1 == j) or (i + 1 == j):
				if arr[i][j] == 0:
					print('arr[i][j] == 0')
					return -1
			else:
				if arr[i][j] != 0:
					print('arr[i][j] != 0')
					return -1
	a, b, c = [], [], []
	for i in range(n):
		b.append(arr[i][i])
		if i != 0:
			a.append(arr[i][i - 1])
			c.append(arr[i - 1][i])
	return tuple(map(np.array, (a, b, c)))