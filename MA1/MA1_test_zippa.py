# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_zippa(self):
        print('\nTests zippa')
        self.assertEqual(zippa([],
                               ['this', 'list', 'is', 'unchanged']),
                         ['this', 'list', 'is', 'unchanged'])
        self.assertEqual(zippa([1, 3, 5],
                               [2, 4, 6]),
                         [1, 2, 3, 4, 5, 6])
        self.assertEqual(zippa(['a', 'b', 'c'],
                               [2, 4, 6, 'x', 10]),
                         ['a', 2, 'b', 4, 'c', 6, 'x', 10])
        self.assertEqual(zippa([['sublist'], 4],
                               ['str']),
                         [['sublist'], 'str', 4])


if __name__ == "__main__":
    unittest.main()
