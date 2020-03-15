import math

# Test Fuction User-defined
def sum_range(begin,end):
    sum = 0
    for i in range(begin,end+1):
        sum += i
    print(f'เริ่ม{begin} สุดท้าย{end}')
    print(sum)

sum_range(1,10) # 55

#parameter คือการรับข้อมูลเข้ามาใน Fuction
#argument คือค่าที่ส่งค่าให้กับ parameter

############### Lambda #############
a = lambda x : print(x)
a(10) #10

square = lambda a: a**2 
sq = square(10) ;print(sq) #100 

net_pay = lambda p , q :print('รวมเป็นเงิน:',p*q)
net_pay(10,20)



def calculate(a,b,add):
    add = a+b
    return a,b,add

add = lambda x,y : x+y
a = calculate(10,20,add) ; print(a)








