import string

def stringToNum(chars):
    return [string.ascii_lowercase.index(char) for char in chars]

def numString(nums):
    return [string.ascii_lowercase[num] for num in nums]

def numstr(key):
    k = []
    for num in key:
        k += [int(num)]
    return k

# k numToString(numstr('43785018456823945619510017465812947'))

def hexToString(nums):
    return nums.decode("hex")

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

def diff(a, b):
    return (ord(a) - ord(b) + 13) % 26 - 13

# print diff('t', 'a')
