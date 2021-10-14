#author Kollen Gruizenga
#function to search list of numbers L for target number T

def findTarget(L, T):
    for x in L:
        if (x == T):
            return True
    return False
