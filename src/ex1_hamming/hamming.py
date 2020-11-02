class Hamming:
    def distance(self, string1, string2):
        difference = 0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                difference += 1
        return difference

