import math
a = format(12345,',')
print(a)
b = format(12344,'_')
print(b)

#polygon_area

n = int(input('จำนวนด้าน:'))
s = float(input('ความยาวแต่ละด้าน:'))
n1 = (n*pow(s,2))
pi1 = 4*math.tan(math.pi/n)
a1 =float(n1/pi1)
print('ค่าที่ได้:',format(a1,'.2f'))

