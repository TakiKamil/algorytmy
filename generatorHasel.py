import random

def generatePassword(lengthOfPassword):
    NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    LOWERLETTERS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    UPPERLETTERS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    SYMBOLS = ('!', '@', '#', '$', '%', '^')
    ALL = NUMBERS + LOWERLETTERS + UPPERLETTERS + SYMBOLS
    lengthOfAll = len(ALL)
    password = ''
    for i in range(0, int(lengthOfPassword)):
        password = password + ALL[random.randrange(0, lengthOfAll - 1)]

    return password

for x in range(50):
    print(f'{x}:{generatePassword(16)}')
