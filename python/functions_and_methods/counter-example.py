
from collections import Counter



def ransom_note(magazine, ransom):
	return(Counter(ransom) - Counter(magazine)) == {}


if __name__ == '__main__':
    mag="give me one million dollars or else"
    ransom = "give me one million dollars"
    print(ransom_note(mag,ransom))

    ransom="give me one billion dollars or else"
    print(ransom_note(mag,ransom))
