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

    def test_verse_5(self):
        self.assertEqual(Xmas.get_verse(5), 'On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_verse_6(self):
        self.assertEqual(Xmas.get_verse(6), 'On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_verse_7(self):
        self.assertEqual(Xmas.get_verse(7), 'On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_verse_8(self):
        self.assertEqual(Xmas.get_verse(8), 'On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')


if __name__ == '__main__':
    unittest.main()
