#author Kollen Gruizenga
#function to decrypt Caesar cipher with int n
def decrypt(n, p):
    alph = 'abcdefghijklmnopqrtsuvwxyz'

    if len(p) == 0:
        return ''
    else:
        return alph[alph.index(p[0]) - n] + decrypt(n, p[1:])
