'''
count_vowels("Celebration") ➞ 5

count_vowels("Palm") ➞ 1

count_vowels("Prediction") ➞ 4
'''

def count_vowels(txt):
    sum = 0
    s = ['a','e','i','o','u']
    for i in range(0,len(s)): 
        sum += txt.lower().count(s[i])
    return sum

count_vowels('Prediction') #4 



