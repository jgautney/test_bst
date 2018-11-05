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

	def test_has_children(self):
		'''
		BinarySearchTree has left and right children
		'''
		bst = BinarySearchTree()
		children = None
		self.assertTrue(bst, bst.children())

	def test_has_insert(self):

		'''
		Test to see if inarySearchTree has insert method
		'''
		bst = BinarySearchTree()
		self.assertTrue(bst, bst.insert())




if __name__ == '__main__':
	unittes.main()