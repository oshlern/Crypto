import general

def encrypt(msg,key):
    # if type(key) != int
    #     if type(key) == float or type(key) == long:
        # key = int(key)
    cypher = ''
    for char in msg:
        cypher += general.increase(char, key)
    return cypher

def decrypt(cypher, key):
    return encrypt(cypher, -1 * key)
