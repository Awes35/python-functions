#author Kollen Gruizenga
#function to search list of numbers L for target T, returning
#index of T occurrence, -1 otherwise

def findTargetIndex(L, T):
    count = -1
    for x in range(len(L)):
         if (L[x] == T):
             count = x
    return count
