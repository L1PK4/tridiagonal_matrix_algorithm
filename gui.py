import sys
from PyQt5.QtWidgets import QSlider, QTableWidgetItem, QWidget, QTableWidget, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
import pickle
import numpy as np
# Importing an algorithm module
import algorithm

class GUI(QWidget):
	'''
	Class of gui for inputing matrix
	'''
	def __init__(self, n = 5):
		super().__init__()
		self.n = n
		self.__init()
	
	def __init(self):
		self.table_A = QTableWidget(self.n, self.n)
		self.table_b = QTableWidget(self.n, 1)
		self.table_x = QTableWidget(1,self.n)
		self.sl = QSlider(Qt.Horizontal)
		self.sl.setMinimum(2)
		self.sl.setMaximum(6)
		pb = QPushButton('Calculate')
		hb1 = QHBoxLayout()
		hb1.addWidget(self.table_A, 1000)
		hb1.addWidget(self.table_b)
		hb2 = QHBoxLayout()
		hb2.addWidget(self.table_x)
		hb2.addWidget(pb)
		vb = QVBoxLayout()
		vb.addLayout(hb1)
		vb.addLayout(hb2)
		vb.addWidget(self.sl)
		self.table_x.setFixedHeight(80)
		self.table_b.setFixedWidth(120)
		self.setGeometry(100, 100, 800, 400)
		self.setLayout(vb)
		pb.clicked.connect(self.calculate)
		self.sl.valueChanged.connect(self.upd)
		for i in range(self.n):
			self.table_b.setItem(i, 0, QTableWidgetItem('1'))
			for j in range(self.n):
				self.table_A.setItem(i, j, QTableWidgetItem('1' if (i == j) or (i - 1 == j) or (i + 1 == j) else '0'))
		# TODO: Make connection between table and algo

	def upd(self):
		self.n = self.sl.value()
		self.table_A.setRowCount(self.n)
		self.table_A.setColumnCount(self.n)
		self.table_b.setRowCount(self.n)
		self.table_x.setColumnCount(self.n)

	def __get_data_A(self):
		try:
			return np.array([[float(self.table_A.item(j, i).text()) for i in range(self.n)] for j in range(self.n)], dtype=float)
		except:
			print("ERR")
			return np.eye(self.n, self.n)
	
	def __get_data_b(self):
		try:
			return np.array([float(self.table_b.item(i, 0).text()) for i in range(self.n)], dtype=float)
		except:
			print("ERR")
			return np.ones(self.n)
	def calculate(self):
		self.print_test()
		a, b, c = algorithm.matrix_to_3list(self.__get_data_A())
		d = self.__get_data_b()
		x = algorithm.algo(a, b, c, d)
		for i in range(self.n):
			self.table_x.setItem(0, i, QTableWidgetItem(str(x[i])))

	def print_test(self):
		print(self.__get_data_A())
		print(self.__get_data_b())

	def start(self, app):
		self.show()
		sys.exit(app.exec_())