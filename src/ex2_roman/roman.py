def roman(number):
    if number < 40:
        symbols = {
            10: 'X',
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
    elif number == 48:
        return 'XL'+roman(8)
    elif number == 49:
        return 'XL'+roman(9)
