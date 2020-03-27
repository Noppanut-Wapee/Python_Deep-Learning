'''
Given that:
  - "A" char code is: 65
  - "a" char code is: 97

counterpartCharCode("A") ➞ 97

def XO(text):
  return text.lower().count('x') == text.lower().count('o')
'''



def counterpartCharCode(char):
    print(char.islower())

    if char.islower() == True:
      print('1')
      print(ord(char.upper()))
      return ord(char.upper())
    else :
      print('2')
      print(ord(char.lower()))
      return ord(char.lower())

counterpartCharCode('a')

def counterpartCharCode(char):
	return ord(char.swapcase())

#counterpartCharCode('A')

