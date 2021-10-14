#author Kollen Gruizenga
#function to compute whether any 2 numbers in integer list L
#sum to equal specified integer N

def sumToN(L, N):
    for x in range(len(L)):
         for y in range(x+1, len(L)):
             if (L[x]+L[y] == N):
                 return True
    return False


    
