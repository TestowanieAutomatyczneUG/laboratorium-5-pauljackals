class Xmas:

    __gifts = [
        ('first', 'a Partridge in a Pear Tree'),
        ('second', 'two Turtle Doves'),
        ('third', 'three French Hens'),
        ('fourth', 'four Calling Birds'),
        ('fifth', 'five Gold Rings'),
        ('sixth', 'six Geese-a-Laying'),
        ('seventh', 'seven Swans-a-Swimming'),
        ('eighth', 'eight Maids-a-Milking'),
        ('ninth', 'nine Ladies Dancing'),
        ('tenth', 'ten Lords-a-Leaping'),
        ('eleventh', 'eleven Pipers Piping'),
        ('twelfth', 'twelve Drummers Drumming'),
    ]

    @classmethod
    def __text(cls, index):
        verse = 'On the ' + cls.__gifts[index][0] + ' day of Christmas my true love gave to me: '
        for i in range(index, -1, -1):
            if i == 0 and index > 0:
                verse += 'and '
            verse += cls.__gifts[i][1]
            if i == 0:
                verse += '.'
            else:
                verse += ', '
        return verse

    @classmethod
    def get_verse(cls, number):
        if 1 <= number <= len(cls.__gifts):
            return cls.__text(number-1)

    @classmethod
    def get_verses(cls, start, end):
        if 1 <= start <= end <= len(cls.__gifts):
            string = ''
            for i in range(start, end+1):
                string += cls.get_verse(i)
                if i != end:
                    string += '\n\n'
            return string
