"""
reverse(True) ➞ False

reverse(False) ➞ True

reverse(0) ➞ "boolean expected"

reverse(None) ➞ "boolean expected"

"""

def reverse(arg):
    
    a = format(not bool(arg))
    return a 

reverse(0)

