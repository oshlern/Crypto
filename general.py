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


# def inputEncrypt():
#     msg = raw_input("Please enter message: ")
#     key = int(raw_input("Please enter key: "))
#     print encrypt(msg, key)

# inputEncrypt()
