#author Kollen Gruizenga
#function to return all words in list L who start with letter "let"

def beginWith(L, let):
    result = []
    for x in L:
        if (x[0] == let):
            result += [x]
    return result
