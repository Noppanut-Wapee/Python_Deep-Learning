#Typer python
#Int ‘1,2,3,’
#Float ‘2.3,3.3’
#Srt ‘ “hello”, “total” ‘
#List [ 10 ,”hello” , 2.3 ]
#Dict {“name” : “Pun”}
#Tup [ 10 ,”hello” , 2.3 ]
#Set {“a”,”b”}
#Bool true , false

#-----------------------------#
"""
print('',3%2)
print('',12)
x = 10
print ('',x)
print('',type(x)) #บอกชนิด type
my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print('',my_taxes)
print('',type(my_income))
"""
#------------string----------------#
#index character , Reverse index
#len นับจำนวน character
"""
name_home =  "i,m \n going a swim"
print('',name_home)
print('',len(name_home))

mystring = 'GOHOME'
print('',len(mystring))
print('',mystring[5])
print('',mystring[-1])
print('',mystring[2:])
print('',mystring[:2])
print('',mystring[1:4])
print('',mystring[ 0: 1:3])
print('',mystring[::-1])
"""
"""
name_1 = 'Hello World'
print ('',name_1[1:])
name_2 = name_1[1:]
print('','T'+name_2) #การบวก string
print('','1'+'12') 
name_3 = name_1 * 10 #การทำซ้ำ string
print('',name_3)

print ('',name_1.upper()) #ทำ string ให้เป็นตัวใหญ่ทั้งหมด
print ('',name_1.lower()) #ทำ string ให้เป็นตัวเล็กทั้งหมด
print ('',name_1.split()) #แยกคำออก โดยใช้ SpacBar
print ('',name_1.split('l'))

"""


# ----------Format {value,width,precisin}---------#
"""
print('This is a string {}'.format('12'))
print('THE {2} {0} {1}'.format('A' ,'B', 'C'))
print('THE {A} {B} {C}'.format(A='1',B='2',C='3'))

total = 100/700
print('The result',total)
print('The result {A}'.format(A=total))
print('The result {B:1.3f}'.format(B=total)) #ปัดเศษให้ด้วย

name_a = 'Pun'
age = '29'
print('my name is {}'.format(name_a))
print(f'my name is {name_a}')
print(f'my name {name_a} {age} years old.')
"""

#-----------------LIST---------------
"""
my_list = [1,2,3,'2']
my_list1 =[ 'one' , 'two' , 'three']
print('',len(my_list))
print ('',my_list+my_list1)
my_list[0]='go home'
print ('',my_list)

my_list.append('SIX') #.append เพิ่ม string ใน str เดิม หรือ Int ก็ได้นะ
print('',my_list)
new_list = my_list.pop(2) # .pop คือการเอาออก
print('',my_list) 

my_list2 = ['a','b','c','e','d']
my_list3 = [2,200,43,5]

my_list4 = my_list3.sort() #.sort เรียงน้อยไปมาก
print ('',my_list4)
"""
#-------------Dictionaries--------------
"""
my_dict = {'key1':'value1','key2':'value2'}
print ('',my_dict)
print('',my_dict['key1'])

prices_lookup = {'apple':'2.99','oranges':'1.99','milk':'5.80'}
print('',prices_lookup['milk'])

a1 = [1,2,3]
print('',type(a1))
a2 = {'ff':100}
print('',type(a2))

d = {'k1':123,'k2':[0,1,2],'k3':{'insidekey':100}}
print('',type(d))
print('',d['k3'])
print('',d['k3']['insidekey'])

print('',d.keys())
print('',d.values())
print('',d.items())
"""
#-----------------Tuples--------------
"""
t = (1,2,3,)
mylist = [1,2,3] 
print('',type(t)) #tuple
print('',type(mylist)) #list
print('',len(t))

a = ('one' , 2 ,3)
print('',a[-1])

t = ('2','2','3')
print('',t.count('3')) #.count นับจำนวน
print('',t.index('2'))  #ชี้ตำปหน่ง

# t[0] = 'one' การแก้ไขแบบนี้ไม่ได้ สำหรับ tuple
# mylist[0] = 'one' ได้ (list)
"""

#--------------SETS-------------------
# SUBSET
"""
myset = set()
print('',myset)
myset.add(1)
print('',myset)
myset.add(2)
print('',myset)

mylist = [1,2,3,1,2,3,4,1,2,3,6,7,9,]
print('',set(mylist)) #โชวค่าซับเซต
"""
#--------- Booleans -----------
"""
True
False
print('',type(False)) #class 'Bool'
print('{}'.format(1>2))
"""

print ('github') #g



