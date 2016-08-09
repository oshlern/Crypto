import general, string

def encrypt(msg,key):
    # if type(key) != int
    #     if type(key) == float or type(key) == long:
        # key = int(key)
    cypher = ''
    for char in msg:
        cypher += increase(char, key)
    return cypher

def decrypt(cypher, key):
    return encypt(cypher, -1 * key)

def inputEncrypt():
    msg = raw_input("Please enter message: ")
    key = int(raw_input("Please enter key: "))
    print encrypt(msg, key)

inputEncrypt()
