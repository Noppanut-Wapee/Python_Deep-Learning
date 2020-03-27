
def cap_to_front(s):
    print(len(s))
    i = 0
    x = ''
    y = ''
    for i in range(0,len(s)):
        print(i)
        
        if s[i].isupper() == True:
            x = x+s[i]
            #print(x)
        elif s[i].islower() == True:
            y = y+s[i]
            #print(y)
    return x+y


cap_to_front('tukKY')
