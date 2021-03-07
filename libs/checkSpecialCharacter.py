import re


def checkSpecialCharacter(strValue):
    if (re.search(r"\^-", strValue)):
        return int(strValue.replace('-', '').replace('px', ''))/(-1)
    else:
        return int(strValue.replace('px', ''))


if __name__ == "__main__":
    x = '-100px'
    newX = checkSpecialCharacter(x)
    print(newX)
