# Dictionary จะมี Key,Value ใช้ {}
# Key จะเป็น String หรือ Int ก็ได้ แต่ห้ามซ้ากัน
# Value เป็นข้อมูลชนิดใดก็ได้

odd_evens = {'odd':[1,3,5,7],'even':[2,4,6,8]}

a = odd_evens['odd'][1] ; print(a) # 3
b = odd_evens['even'][2] ; print(b) # 6

ranger = {'a':range(0,5),'b':range(6,10)} ; print(type(ranger)) 
e = ranger['b'][2] ; print(e) # 8

countries = {'th':'Thailand','jp':'Japan'}
for key in countries:
    print(countries[key]) # print value โดยใช้ Key

# in กับ Dictionary
countries = {'th':'Thailand','jp':'Japan','kr':'Korea'}
a = 'th' in countries ;print(a) #True

print(len(countries)) #3
del countries['kr']
print(len(countries)) #2

# function item
info = {'name':'jhon', 'age':30 ,'height':170,'single':True}
for (i,v) in info.items():
    print(f'{i},{v}')

# function get pop
count = {'one':'หนึ่ง','two':'สอง','three':'สาม'}
print(count.get('three')) # get อ่านค่า Value ตามที่ key กำหนด
print(count.pop('two')) # pop อ่านค่า Valie ตาม key แล้วลบค่าที่อ่านด้วย
print(len(count)) # 2
print(count.items()) # 'two':'สอง' หายไปแล้ววววว



