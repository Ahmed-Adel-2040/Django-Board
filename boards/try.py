def exchange(word):
    length =len(word)
    revers=""
    lastIndex=length-1 # get the last letter index in word
    for index in range(length):
        revers = revers + word[lastIndex]
        lastIndex -= 1

    return revers
"""
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""
def password_Confirmation(pasword=""):
    small_letter=Capital_letter=isNumber=issign=False
    sign=["$","#","@"]
    if len(pasword) > 16 or len(pasword) < 6:
        print("the length of password  does not match our terms")
        return False
    for letter in pasword:
        if letter.isdigit():
            isNumber = True
        if letter.isupper():
            Capital_letter = True
        if letter.islower():
            small_letter = True
        if letter in sign:
            issign = True
    if issign and Capital_letter and small_letter and isNumber == True:
        return True
    else:
        return False
pasword="Aas$df1dsffds"
answer=password_Confirmation(pasword)
print("the password is ",answer)



