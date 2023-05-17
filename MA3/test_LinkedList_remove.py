"""
Unittests for the linked lists remove
"""

import unittest

from linked_list import *


class Test(unittest.TestCase):
    def test_remove(self):
        print("\nTests remove")
        lst = LinkedList()
        for x in [3, 1, 2, 6]:
            lst.insert(x)

        self.assertEqual(lst.remove(0), False)
        self.assertEqual(lst.to_list(), [1, 2, 3, 6])

        self.assertEqual(lst.remove(3), True)
        self.assertEqual(lst.to_list(), [1, 2, 6])

        self.assertEqual(lst.remove(6), True)
        self.assertEqual(lst.remove(2), True)
        self.assertEqual(lst.remove(1), True)
        self.assertEqual(lst.to_list(), [])

        self.assertEqual(lst.remove(2), False)

        self.assertEqual(lst.first, None)


if __name__ == "__main__":
    unittest.main()
