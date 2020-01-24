from proj.sample_module import add2num

import unittest

class SampleTest(unittest.TestCase):

	# simple exception raise
	def test_raise_exception(self):
		self.assertRaises(TypeError, add2num, 2, 'Hello')

	@unittest.skip('Testing skipping test cases')
	@unittest.skipIf(1==2 ,'Testing skipping test cases')
	@unittest.skipUnless(1==2 ,'Testing skipping test cases')
	def test_raise_exception_detail(self):
		with self.assertRaises(TypeError) as e:
			r = add2num(2, 'Hello')
			self.assetEqual(str(e.exception), "unsupported operand type(s) for +: 'int' and 'str'")


	@unittest.expectedFailure
	def test_raise_exception_detail(self):
		with self.assertRaises(ValueError) as e:
			r = add2num(2, 'Hello')
			self.assetEqual(str(e.exception), "unsupported operand type(s) for +: 'int' and 'str'")