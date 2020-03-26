'''
import math
import random

a = random.randint(1,1000000)
print(a)
#a = 74913
b = a//3600
c = a%3600
d = c//60
e = c%60
print(f'เวลาทั้งหมด:{a} วินาที >>>> {b} ชั่วโมง {d} นาที {e} วินาที')
'''

# import os
# import time
from random import randint
# ---------------------------

def guessme(x):
    
    ans = randint(1,5)

    if x < ans:
        # print("Less")
        print(x)
        return False
    elif x > ans and x <=5:
        print("More")
        return False
    
    elif x > 5:
        # print(exit)
        return 'exit'
    
    else:
        # print("Correct")
        return True


if __name__ == "__main__":
    score = 0
    while True:
        x = int(input("Please enter Integer number : "))


        flag = guessme(x)


        if flag == range(1,6):
            score += 1
            print(score)
            #print('111')
        elif flag == 'exit' :
            #print('222')
            print("Your Score {}".format(score))
            print("Exit")
            break
        else:
           # print('333')
            print("Again")
        
    

    # Python code to demonstrate naive method 
# to compute factorial 
n = int(input('ใส่เลข Fac:'))

fact = 1

for i in range(1,n+1): 
	fact = fact * i 
	
print ("The factorial is {n}:{fact}  ".format(n=n,fact=fact)) 
print (fact) 
