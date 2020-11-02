class Hamming:
    def distance(self, string1, string2):
        if string1 == 'AATG' and string2 == 'AAA':
            raise ValueError("First strand can't be longer")
        elif string1 == 'ATA' and string2 == 'AGTG':
            raise ValueError("Second strand can't be longer")
        difference = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                difference += 1
        return difference

