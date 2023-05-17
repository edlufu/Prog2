# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):
    def test_multiply(self):
        print("\nTests multiply")
        self.assertEqual(multiply(2, 5), 10)
        self.assertEqual(multiply(5, 2), 10)
        self.assertEqual(multiply(1, 5), 5)
        self.assertEqual(multiply(9, 0), 0)

    def test_multiply_effectivity(self):
        print("\nTests multiply effectivity")
        self.assertEqual(multiply(200, 500), 100000)
        self.assertEqual(multiply(50000000000, 20000000000), 1000000000000000000000)
        self.assertEqual(
            multiply(1000000000000000000000000000000000000, 5),
            5000000000000000000000000000000000000,
        )
        self.assertEqual(multiply(90000000, 0), 0)


if __name__ == "__main__":
    unittest.main()
