#author Kollen Gruizenga
#recursive function to move all "Z" chars in string S to the end

def endZ(S):
    if len(S) == 0:
        return ''
    elif S[0] == 'Z':
        return endZ(S[1:]) + S[0]
    else:
        return S[0] + endZ(S[1:])
