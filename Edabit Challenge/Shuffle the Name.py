'''
name_shuffle("Donald Trump") ➞ "Trump Donald"

name_shuffle("Rosie O'Donnell") ➞ "O'Donnell Rosie"

name_shuffle("Seymour Butts") ➞ "Butts Seymour"
'''
def name_shuffle(txt):
    txt = txt.split()
    return print(txt[1]+' '+txt[0])

name_shuffle("Donald Trump")



