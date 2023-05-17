# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_count(self):
        print('\nTests count')
        print('\nAtt sökning i tom lista ger 0.')
        self.assertEqual(count(1, []), 0)

        print('OK\nAtt även första och sista elementen i listan kontrolleras.')
        self.assertEqual(count('end', ['end', 1, 3, 5, 'end']), 2)

        print('OK\nAtt det går att söka efter listor.')
        self.assertEqual(
            count(['a', 'list'], [['a', 'list'], 2, 6, 'b', ['wrong', 'list']]), 1)

        print('OK\nAtt sublistor på flera nivåer genomsöks.')
        self.assertEqual(
            count(4, [1, [4, 4], 3, 1, 4, 2, ['a', [[4, 4], 4, 4]]]), 7)

        print('OK\nAtt sökning efter icke existerande element ger 0.')
        self.assertEqual(count(1, ['no', 'ones', 'in', 'here', 2, 3, 4, 5]), 0)

        print('OK\nAtt den sökta listan inte förstörs.')
        og_list = ['bla', 'bla', 'bla']
        dummy_list = og_list.copy()
        count('bla', dummy_list)
        self.assertEqual(dummy_list, og_list)
        print('OK')


if __name__ == "__main__":
    unittest.main()
