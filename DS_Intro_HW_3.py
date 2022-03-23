# Gal Giller 209264555
# 1
def read_line(n, file):
    try:
        data1 = open(file)
        if type(n) == int:
            counter = 0
            for line in data1:
                counter += 1
                if n == counter:
                    return line
            return "line " + str(n) + " doesn't exist"
        else:
            return "invalid input detected"
    except:
        return "file not found"

# 2
import re
def longest_words(file):
    try:
        data2 = open(file)
        data2 = data2.read()
        data_words = re.sub('\W+', ' ', data2)
        words = data_words.split()
        DSC = []
        DSC = sorted(words, key=len, reverse=True)
        return DSC[0:5]
    except:
        print ("file not found")
        return []
