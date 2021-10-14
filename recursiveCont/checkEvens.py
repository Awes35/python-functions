#author Kollen Gruizenga
# recursive function to check whether all int's in list L are even

def allEven(L):
    if len(L) == 0:
        return True
    elif L[0] % 2 == 0:
        return allEven(L[1:])
    else:
        return False

