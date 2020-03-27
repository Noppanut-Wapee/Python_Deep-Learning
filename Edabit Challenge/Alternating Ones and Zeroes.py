def can_alternate(s):
    x = 0
    y = 0 
    print(len(s))
    for i in range(0,len(s)):
        if s[i] in '1':
            x += 1
            print(x)
        else:
            y += 1
            print(y)

    if abs(x-y) <= 1:
        print('True')
        return True
    else:
        print('False')
        return False

can_alternate('010001')   
    
    
    
    