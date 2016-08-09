import general

def encrypt(msg,key):
    key = general.stringToNum(key)
    cypher = ''
    for i in range(len(msg)):
        cypher += general.increase(msg[i], key[i%len(key)])
    return cypher

def decrypt(crypt, key):
    key = general.stringToNum(key)
    msg = ''
    for i in range(len(crypt)):
        msg += general.increase(crypt[i], -1 * key[i%len(key)])
    return msg
