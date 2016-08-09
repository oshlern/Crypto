import caesar

def caesarBreak(crypt):
    print "\n\n~~~~~~~~~~~~~~~~~~~~BREAKING CAESAR~~~~~~~~~~~~~~~~~~~~~"
    for i in range(26):
        print ' '*i, caesar.decrypt(crypt, i), '\n\n'
    return 0

def vigenereBreak(crypt):
    print "\n\n~~~~~~~~~~~~~~~~~~~~BREAKING CAESAR~~~~~~~~~~~~~~~~~~~~~"
    for i in range(26):
        print ' '*i, caesar.decrypt(crypt, i), '\n\n'
    return 0

# caeserBreak('BC cn\'m gy C fcey jcttu')
