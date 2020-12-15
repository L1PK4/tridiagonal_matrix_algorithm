import sys
from PyQt5.QtWidgets import QWidget, QTableWidget, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
import pickle
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
		self.setGeometry(100, 100, 800, 400)
		self.setLayout(vb)
		# TODO: Make connection between table and algo

	def __get_data(self):
		return self.table_A.
	
	def start(self, app):
		self.show()
		sys.exit(app.exec_())