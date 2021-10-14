#author Kollen Gruizenga
#function to encrypt via Caesar cipher using key alph and user input num
def encrypt(num, s):
    alph = 'abcdefghijklmnopqrtsuvwxyz'

    if len(s) == 0:
        return ''
    else:
        if (alph.index(s[0]) + num) > 25:
            return alph[alph.index(s[0]) + num - 26] + encrypt(num, s[1:])
        else:
            return alph[alph.index(s[0]) + num] + encrypt(num, s[1:])
