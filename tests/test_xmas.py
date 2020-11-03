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

    def test_verse_9(self):
        self.assertEqual(Xmas.get_verse(9), 'On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_verse_10(self):
        self.assertEqual(Xmas.get_verse(10), 'On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_verse_11(self):
        self.assertEqual(Xmas.get_verse(11), 'On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_verse_12(self):
        self.assertEqual(Xmas.get_verse(12), 'On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_verses_2_to_4(self):
        self.assertEqual(Xmas.get_verses(2, 4), 'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\n\n'
                                                'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n'
                                                'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_verses_8_to_8(self):
        self.assertEqual(Xmas.get_verses(8, 8), 'On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_verses_all(self):
        self.assertEqual(Xmas.get_verses_all(), 'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\n\n'
                                                'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\n\n'
                                                'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n'
                                                'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n'
                                                'On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n'
                                                'On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n'
                                                'On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n'
                                                'On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n'
                                                'On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n'
                                                'On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n'
                                                'On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n'
                                                'On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_verse_out_of_range(self):
        with self.assertRaises(IndexError):
            Xmas.get_verse(-1)

    def test_verse_wrong_type(self):
        with self.assertRaises(TypeError):
            Xmas.get_verse([])

    def test_verses_start_bigger_than_end(self):
        with self.assertRaises(ValueError):
            Xmas.get_verses(7, 2)

    def test_verses_out_of_range(self):
        with self.assertRaises(IndexError):
            Xmas.get_verses(5, 14)


if __name__ == '__main__':
    unittest.main()
