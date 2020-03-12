import math
import random
a = math.ceil(1.2) ; print(f'จำนวนเต็มที่อยู่ถัดไป : {a}')
b = math.floor(12.55); print(f'จำนวนเต็มที่อยู่ก่่อนค่าที่ระบุ : {b}')
c = math.factorial(10) ; print(f'ค่า fac ! :{c} ')
d = float(input('ค่า root :')) ; print('ค่ารากที่สอง : ',math.sqrt(d))
a1 = 100.99 ; e = math.trunc(a1) ; print(f'ค่าจำนวนเต็มตัดเศษทิ้งหมด : {e}')
f = math.fmod(-19,4) ; print(f'หารแล้วเอาเฉพาะเศษ : {f}') # -19 % 4 = 1 (น้อยกว่า -19 คือ -20)
t = float(input('ค่าที่จะแยกทศนิยมกับจำนวนเต็ม:')) ; t1 = math.modf(t); print(f'ค่าจำนวนเต็ม:{t1[1]},ค่าทศนิยม:{t1[0]}')
h = math.sin(math.pi/2) ; print('ค่า sin (pi/2):',h)

r1 = random.random() ; print('ค่าสุ่ม 0-1',r1)
r2 = random.randint(10,20) ; print('ค่าสุ่ม 10-20:',r2)
r3 = random.choice('การบ้าน') ; print('การบ้าน',r3)

