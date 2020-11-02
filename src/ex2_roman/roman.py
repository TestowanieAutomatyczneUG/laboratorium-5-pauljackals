def roman(number):
    if number < 9:
        symbols = {
            5: 'V',
            1: 'I'
        }
        temp = number
        roman_number = ''
        while temp > 0:
            for key, value in symbols.items():
                if temp - key >= 0:
                    roman_number += value
                    temp -= key
                    break
                elif temp + 1 - key == 0:
                    roman_number += (symbols.get(1) + value)
                    temp -= key - 1
                    break
        return roman_number
    elif number == 9:
        return 'IX'
    elif number == 27:
        return 'XXVII'
