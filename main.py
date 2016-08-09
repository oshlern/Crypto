import caesar, crackCyphers, vigenere

cyphers = ["caesar", "vigenere"]

def encrypt(cypher, msg, key):
    crypt = ''
    if cypher == "caesar":
        crypt = caesar.encrypt(msg, int(key))
    elif cypher == "vigenere":
        crypt = vigenere.encrypt(msg, key)
    else:
        print 'cypher not found'
        return 0
    return crypt

def decrypt(cypher, crypt, key):
    msg = ''
    if cypher == "caesar":
        msg = caesar.decrypt(crypt, int(key))
    elif cypher == "vigenere":
        msg = vigenere.decrypt(crypt, key)
    else:
        print 'cypher not found'
        return 0
    return msg

def crack(cypher, crypt):
    if cypher == "caesar":
        crackCyphers.caesarBreak(crypt)
    elif cypher == "vigenere":
        crackCyphers.vigenereBreak(crypt)
    else:
        print 'cypher not found'
        return 0

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

def inputEncrypt():
    cypher = inputCypher()
    msg = raw_input("Please enter message: ")
    key = raw_input("Please enter key: ")
    print encrypt(cypher, msg, key)

def inputDecrypt():
    cypher = inputCypher()
    crypt = raw_input("Please enter message: ")
    key = raw_input("Please enter key: ")
    print decrypt(cypher, crypt, key)

def inputCrack():
    cypher = inputCypher()
    crypt = raw_input("Please enter crypt: ")
    crack(cypher, crypt)

# inputDecrypt()
# inputCrack()
# crack("caesar", "wtip qba WAPMZ pwe'a qb owqvo?")
print decrypt('vigenere','hfnlp','abc')
