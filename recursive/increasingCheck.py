#Kollen Gruizenga
#recursive function to return boolean value for whether
# list of int L is sorted ascending

def increasing(L):
    if len(L) <= 1:
        return True
    elif L[0] <= L[1]:
        return increasing(L[1:])
    else:
        return False
