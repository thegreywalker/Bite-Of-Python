def longestWord(ls : list) -> str:
    lengthOflargestWord = len(ls[0])
    wordIndex = 0
    for index, val in enumerate(ls):
        if len(val) >= lengthOflargestWord:
           wordIndex = index
           lengthOflargestWord = len(val)
        else:
            lengthOflargestWord = lengthOflargestWord
            wordIndex = wordIndex
    return ls[wordIndex]



def FiboinTuple() -> tuple:
    ls = [0, 1]
    for val in range(1, 8):
        ls.append(ls[-1] + ls[-2])
    return tuple(ls)


def commonElements(ls: list, ls2: list) -> list:
    Commonlist = []
    for val in ls:
        for element in ls2:
            if val == element:
                Commonlist.append(val)
            else:
                pass
        
        else:
            continue
    return Commonlist


class Dictionary():
    def __init__(self) -> None:
        self.dictionary = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'Octobar': 31,
        'Novembar': 30,
        'Decembar': 31
    }

    def getDays(self, month) -> str:
        return "The Number of Days in {0} is {1}".format(
            month, self.dictionary[month]
        )
    
    def getMonths(self) -> list:
        listOfMonths = []
        for val in self.dictionary.keys():
            if self.dictionary[val] == 31:
                listOfMonths.append( "{0}".format(val))
        return listOfMonths


def getDigits(number : int) -> int:
    nm = number
    count = 0
    for val in range(len(str(number))):
        number //= 10
        count += 1
    return "The Number {0} has {1} digits in it.".format(nm, count)



    