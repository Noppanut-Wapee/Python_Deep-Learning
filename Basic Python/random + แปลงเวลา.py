import math
import random

a = random.randint(100000,1000000)
print(a)
#a = 74913
b = a//3600
c = a%3600
d = c//60
e = c%60
print(f'เวลาทั้งหมด:{a} วินาที >>>> {b} ชั่วโมง {d} นาที {e} วินาที')