#author Kollen Gruizenga
#function to find and return index of largest number in list L

def findMaxIndex(L):
    result = L[0]
    largestIndex = 0
    for x in range(len(L)):
         if (L[x] > result):
             largestIndex = x
             result = L[x]
    return largestIndex
