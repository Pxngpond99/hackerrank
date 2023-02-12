def caesarCipher(s, k):
    # Write your code here
    ori_alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_ro = ''
    encrypts = ''
    for i in ori_alpha:
            alpha_ro += ori_alpha[(ori_alpha.index(i)+k)%26]
    for x in s:
        if x.isupper():
            encrypts += alpha_ro[ori_alpha.index(x.lower())].upper()
        elif x in ori_alpha:
            encrypts += alpha_ro[ori_alpha.index(x)]
        else:
            encrypts += x
    return encrypts