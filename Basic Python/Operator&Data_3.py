
'''
sum = 0
sum += int(input('ค่าที่1:'))
sum += int(input('ค่าที่2:'))
sum += int(input('ค่าที่3:'))
sum += int(input('ค่าที่4:'))

ave = sum/4

print(f'ค่าเฉลี่ย = {ave}')

'''
'''
n = int(input('ใส่เลขสี่หลัก:'))
x = n
x //=1000
print (x)

x = n
x %= 1000
x //=100
print (x)

x = n
x %= 100
x //= 10
print (x)

x = n 
x %=10
print (x)

'''

import math
import random

print ('',math.factorial(10))
print('',random.randint(1,10))
print ('',random.random())
print('',random.uniform(10,100))
print('',random.choice('123456789'))
