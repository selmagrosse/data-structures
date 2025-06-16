import unittest
from data_structures.binary_search_tree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()
    
    def test_add_and_contains(self):
        self.assertTrue(self.bst.add(10))
        self.assertTrue(self.bst.add(5))
        self.assertTrue(self.bst.add(15))
        self.assertFalse(self.bst.add(10))  # duplicate, should return False
        
        self.assertTrue(self.bst.contains(10))
        self.assertTrue(self.bst.contains(5))
        self.assertTrue(self.bst.contains(15))
        self.assertFalse(self.bst.contains(100))
    
    def test_size(self):
        self.assertEqual(self.bst.size(), 0)
        self.bst.add(10)
        self.assertEqual(self.bst.size(), 1)
        self.bst.add(5)
        self.assertEqual(self.bst.size(), 2)
        self.bst.add(15)
        self.assertEqual(self.bst.size(), 3)
        
    def test_remove(self):
        self.bst.add(10)
        self.bst.add(5)
        self.bst.add(15)
        self.assertTrue(self.bst.remove(5))
        self.assertFalse(self.bst.contains(5))
        self.assertFalse(self.bst.remove(100))  # removing non-existent element returns False
    
    def test_height(self):
        self.assertEqual(self.bst.height(self.bst.root), -1)
        self.bst.add(10)
        self.assertEqual(self.bst.height(self.bst.root), 0)
        self.bst.add(5)
        self.bst.add(15)
        self.assertEqual(self.bst.height(self.bst.root), 1)

if __name__ == '__main__':
    unittest.main()
