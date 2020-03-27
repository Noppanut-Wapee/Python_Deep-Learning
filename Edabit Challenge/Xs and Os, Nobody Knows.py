def XO(txt):
    
    if txt == '':
	    return True
				
    txt = txt.lower()

    for i in range(0,len(txt)):
        if txt[i] == 'x':
            a += 1
        elif txt[i] == 'o':
            b += 1
        else :
            c += 1
						
    if a == b :
	    return True
    elif a != b :
        return False


def XO(text):
  return text.lower().count('x') == text.lower().count('o')
	