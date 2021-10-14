#author Kollen Gruizenga
#function to return strings in list L that are less than N letters

def lessThanN(L, N):
    result = []
    for x in L:
        if (len(x) < N):
            result += [x]
    return result
