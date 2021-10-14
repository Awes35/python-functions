#author Kollen Gruizenga
#function to find the largest number in list L

def findMax(L):
    result = L[0]
    for x in L:
        if (x > result):
            result = x
    return result

