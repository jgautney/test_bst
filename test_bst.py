#Run me with 'python -m unittest test_bst'

from bst import BinarySearchTree
import unittest

class TestBinarySearchTree(unittest.TestCase):

	# def test_failure(self):
	# 	self.fail("Intentional failure")

	def test_instantiation(self):
		'''
		A BinarySearchTree exists
		'''
		try:
			BinarySearchTree()
		except NameError:
			self.fail("Could not instantiate BinarySearchtree")


if __name__ == '__main__':
	unittes.main()