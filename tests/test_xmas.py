import unittest
from ex3_xmas.xmas import Xmas


class XmasTest(unittest.TestCase):
    def test_verse_1(self):
        self.assertEqual(Xmas.get_verse(1), 'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.')

    def test_verse_2(self):
        self.assertEqual(Xmas.get_verse(2), 'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_verse_3(self):
        self.assertEqual(Xmas.get_verse(3), 'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_verse_4(self):
        self.assertEqual(Xmas.get_verse(4), 'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')


if __name__ == '__main__':
    unittest.main()
