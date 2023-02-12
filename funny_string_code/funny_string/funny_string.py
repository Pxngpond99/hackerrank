def funnyString(s):
    # Write your code here
    asc = [ord(a) for a in s]
    s = [abs(asc[i]-asc[i+1]) for i in range(len(asc)-1)]
    if s == s[::-1]:
        return "Funny"
    return "Not Funny"