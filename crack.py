import caesar

def caeserBreak(cypher):
    print "\n\n~~~~~~~~~~~~~~~~~~~~BREAKING CAESAR~~~~~~~~~~~~~~~~~~~~~"
    for i in range(26):
        print caesar.decrypt(cypher, i)

print caesarBreak("")
