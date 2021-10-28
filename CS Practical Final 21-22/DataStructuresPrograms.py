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


def dictDatas(*args) -> dict:
    dictionary = {}
    for index, val in enumerate(args):
        if index%2 == 0:
            dictionary[str(val)] = args[index+1]

        else:
            pass
    return dictionary
