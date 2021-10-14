#author Kollen Gruizenga
#recursive function to return a string S where all "Z" char removed

def noZ(S):
    if len(S) == 0:
        return ''
    elif S[0] == 'Z':
        return noZ(S[1:])
    else:
        return S[0] + noZ(S[1:])
 
