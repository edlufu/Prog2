"""
Unittests for the binary search tree methods
"""

import unittest

from bst import *
from linked_list import *


class Test(unittest.TestCase):
    def test_remove(self):
        print("\nTests BST remove")
        bst = BST()
        for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
            bst.insert(x)
        self.assertEqual(bst.to_list(), [1, 3, 4, 5, 6, 7, 8])
        bst.remove(3)
        self.assertEqual(bst.to_list(), [1, 4, 5, 6, 7, 8])
        bst.remove(7)
        self.assertEqual(bst.to_list(), [1, 4, 5, 6, 8])
        bst.remove(6)
        self.assertEqual(bst.to_list(), [1, 4, 5, 8])
        bst.remove(4)
        self.assertEqual(bst.to_list(), [1, 5, 8])


if __name__ == "__main__":
    unittest.main()
