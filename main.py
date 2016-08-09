import caesar, crack#, vig

cyphers = ["caesar", "vigenere"]

def inputCypher():
    c = raw_input("Please enter cypher: ")
    if c.lower() == "caesar" or c.lower() == "ceasar" or c.lower() == "c" or c.lower() == "caeser" or c.lower() == "ceaser":
        return "caesar"
    elif c.lower() == "vig" or c.lower() == "vigenere" or c.lower() == "v":
        return "vigenere"
    else:
        print "----That cypher is not in our records. Please make sure it is spelled correctly"
        print "----Cyphers include: caesar, vigenere"
        return inputCypher()

def encrypt(cypher, msg, key):
    crypt = ''
    if cypher == "caesar":
        crypt = caesar.encrypt(msg, int(key))
    # elif cypher == "vigenere":
    #     crypt = vig.encrypt(msg, key)
    else:
        print 'cypher not found'
        return 0
    return crypt

def inputEncrypt():
    cypher = inputCypher()
    msg = raw_input("Please enter message: ")
    key = raw_input("Please enter key: ")

    print encrypt(cypher, msg, key)

def crack(crypt, cypher):
    if cypher == "caesar":
        print crack.caesarBreak()
    # elif cypher == "vigenere":
    #     print crack.vigenereBreak
    else:
        print 'cypher not found'
        return 0

def inputCrack(crypt):
    cypher = inputCypher()
    crypt = raw_input("Please enter crypt: ")
    crack(cypher, crypt)

# inputEncrypt()
inputCrack()
