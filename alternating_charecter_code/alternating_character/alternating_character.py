def alternatingCharacters(s):
    # Write your code here
    charecter = ''
    result = 0
    for i in s:
        if i != charecter:
            charecter = str(i)
        elif i == charecter:
            result += 1
    return result