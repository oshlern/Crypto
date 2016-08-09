import string

def stringToNum(string):
    return [ord(char) for char in string]

def numArrayToString(num):
    string = ''
    for i in num:
        string += chr(i)
    return(string)

def numToArray(num):
    array = []
    while num != 0:
        digit=num%10
        array.append(digit)
        num=(num-digit)/10
    return array

def numToString(num):
    return numArrayToString(numToArray(num))

def increase(char, key):
    for chars in [string.ascii_lowercase, string.ascii_uppercase]:
        if char in chars:
            char = chars[(chars.index(char) + key) % len(chars)]
            return char
    return char
