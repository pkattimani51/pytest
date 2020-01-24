from proj.sample_module import add2num
from proj.powertonumber import pow2num

import unittest

def setUpModule():
	print('Start - This runs before every Module load....')

def tearDownModule():
	print('End - This runs after end of module....')

class Testadd2num(unittest.TestCase):
	"""docstring for Testadd2num"""

	def setUp(self):
		print('Start - This runs before every methods....')

	def tearDown(self):
		print('End - This runs after every methods....')

	@classmethod
	def setUpClass(cls):
		print('Start - This runs once start of class....')

	@classmethod
	def tearDownClass(cls):
		print('End - This runs after all methods....')

	def test_sum_2pos_num(self):
		self.assertEqual(add2num(5,6), 11)
	
	def test_sum_1pos_1neg_num(self):
		self.assertEqual(add2num(-5,6), 1)

class Testpow2num(unittest.TestCase):

	def setUp(self):
		print('Start - This runs before every methods....')

	def tearDown(self):
		print('End - This runs after every methods....')

	@classmethod
	def setUpClass(cls):
		print('Start - This runs once start of class....')

	@classmethod
	def tearDownClass(cls):
		print('End - This runs after all methods....')

	def test_pow_2pos_num(self):
		self.assertEqual(pow2num(3, 4), 81)

	def test_neg_pow(self):
		self.assertEqual(pow2num(10, -2), 0.01)

	def test_negnum_pow(self):
		self.assertEqual(pow2num(-3, 3), -26)

if __name__ == '__main__':
	unittest.main()