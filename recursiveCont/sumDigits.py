#author Kollen Gruizenga
#recursive function to return sum of digits of number N

    
def sumUpDigits(N):
    if N == 0:
        return 0
    else:
        return (N%10) + sumUpDigits(N//10)
