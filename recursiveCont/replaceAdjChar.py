#author Kollen Gruizenga
#recursive function to return string S where all adjacent chars
#separated by "@"

    
def moreAts(S):
    if len(S) == 0:
        return ''
    elif len(S) == 1:
        return S[len(S)-1]
    else:
        return S[0] + '@' + moreAts(S[1:])

