#author Kollen Gruizenga
#recursive function to check whether there is a nesting of 0+
#pairs of parenthesis. Returns false if incomplete pairs

def nested(S):
    if len(S) == 0:
        return True
    elif len(S) == 1:
        return False
    elif S[0] == '(' and S[-1] == ')':
        return nested(S[1:len(S)-1])
    else:
        return False
