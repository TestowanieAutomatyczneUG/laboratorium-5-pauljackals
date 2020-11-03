class Xmas:

    @staticmethod
    def __text(index):
        numerals = [
            'first',
            'second',
            'third',
            'fourth',
            'fifth',
            'sixth',
            'seventh',
            'eighth',
            'ninth',
            'tenth',
            'eleventh',
            'twelfth'
        ]
        gifts = [
            'a Partridge in a Pear Tree',
            'two Turtle Doves',
            'three French Hens',
            'four Calling Birds',
            'five Gold Rings',
            'six Geese-a-Laying',
            'seven Swans-a-Swimming',
            'eight Maids-a-Milking',
            'nine Ladies Dancing',
            'ten Lords-a-Leaping',
            'eleven Pipers Piping',
            'twelve Drummers Drumming'
        ]
        verse = 'On the ' + numerals[index] + ' day of Christmas my true love gave to me: '
        for i in range(index, -1, -1):
            if i == 0 and index > 0:
                verse += 'and '
            verse += gifts[i]
            if i == 0:
                verse += '.'
            else:
                verse += ', '
        return verse

    @classmethod
    def get_verse(cls, number):
        if 1 <= number <= 12:
            return cls.__text(number-1)
