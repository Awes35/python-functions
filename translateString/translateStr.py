#author Kollen Gruizenga
#functions to translate a string by appending "way" or "ay" to end
#of string, and ensure ensure first letters are vowels, moving consonants

#primary function, other helpers called from here
def translatePL(s):
    if isFirstLetterVowel(s):
        result = s + 'way'
    elif hasTwoConsonantsAsFirst(s):
        result = s[2:] + getFirstLetter(s) + getFirstLetter(getRest(s)) + 'ay'
    else:
        result = getRest(s) + getFirstLetter(s) + 'ay'
    return result

def getRest(s):
    return s[1:]

def getFirstLetter(s):
    return s[0]

def isFirstLetterVowel(s):
    if getFirstLetter(s) in 'aeiou':
        return True
    else:
        return False

def hasTwoConsonantsAsFirst(s):
    if isFirstLetterVowel(s) == True or isFirstLetterVowel(getRest(s)) == True:
        return False
    else:
        return True
    

