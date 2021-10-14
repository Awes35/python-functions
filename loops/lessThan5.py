#author Kollen Gruizenga
#function to return strings in list L that are less than 5 letters

def lessThan5(L):
    result = []
    for x in L:
        if (len(x) < 5):
            result += [x]
    return result
