#author Kollen Gruizenga
#recursive function to count number of times substring "sub"
#appears in string S, without overlap

def strCount(S, sub):
    if len(S) < len(sub):
        return 0
    elif sub in S[0:len(sub)]:
        return 1 + strCount(S[len(sub):], sub)
    else:
        return strCount(S[len(sub):], sub)


