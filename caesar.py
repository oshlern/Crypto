import general

def encrypt(msg,key):
    cypher = stringToNum(msg)
    print cypher
    for i in range(len(cypher)):
        cypher[i] = ((cypher[i] + key - 95) % 26) + 95
    print cypher
    return numArrayToString(cypher)

def decrypt(cypher, key):
    return encypt(cypher, -1 * key)

def inputEncrypt():
    msg = raw_input("Please enter message: ")
    key = int(raw_input("Please enter key: "))
    print encrypt(msg, key)

# inputEncrypt()
