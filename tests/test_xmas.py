import unittest
from ex3_xmas.xmas import Xmas


class XmasTest(unittest.TestCase):
    def test_verse_1(self):
        self.assertEqual(Xmas.get_verse(1), 'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.')


if __name__ == '__main__':
    unittest.main()
