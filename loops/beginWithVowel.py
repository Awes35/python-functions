#author Kollen Gruizenga
#function to return words from list L who start with vowel

def beginWithVowel(L):
    result = []
    for x in L:
        if (x[0] in 'aeiou'):
            result += [x]
    return result
