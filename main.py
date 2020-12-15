import algorithm
import numpy as np
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--test", help="Testing without gui", action="store_true")
args = parser.parse_args()

def main():
	app = QApplication(sys.argv)
	g = gui.GUI()
	g.start(app)

if args.test:
	A = np.array([[10,2,0,0],[3,10,4,0],[0,1,7,5],[0,0,3,4]],dtype=float) 
	a, b, c = algorithm.matrix_to_3list(A)
	d = np.array([3,4,5,6.])
	x = algorithm.algo(a,b,c,d).T
	print(
		f"""
Input array:
{A}
B vector:
{d}
Solution by algo:
{x}
Solution by numpy:
{np.linalg.solve(A,d)}
Residual:
{d - np.matmul(A, x)}
		"""
	)
else:
	import gui
	from PyQt5.QtWidgets import QApplication
	main()
	pass