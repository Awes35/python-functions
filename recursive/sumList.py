#author Kollen Gruizenga
#recursive sum function for list of integers L

def sum(L):
    if len(L) == 0:
        return 0
    else:
        return L[0] + sum(L[1:])
