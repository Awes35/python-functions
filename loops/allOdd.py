#author Kollen Gruizenga
#function to check if all numbers are odd in list L

def allOdd(L):
    for x in L:
        if (x%2 == 0):
            return False
    return True
