#LIST#
list1 = list() 
list2 = list([1,2,3,4,5]) #สมาชิก int 
list3 = list(['one','two','three'])
list4 = list(range(1,10)) ; print(list4) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
list5 = list([1,2,'three']) ;print(list5) # [1,2,'three']
a = ['1,2'] ; print('',list(a)) # ข้อควรระวัง แตกต่างจาก list เพราะจะได้สมาชิกตัวเดียว ['1,2'] 

#การแก้ไขข้อมูลใน list
colors = ['red','yellow','blue'] ; print(colors) #['red', 'yellow', 'blue']
colors[0] = '1' ; print(colors) # ['1', 'yellow', 'blue']

# การใช้ loops กับ list

num1 = [1,2,3,4,5] 
for i in num1:
    print(i)

str1 = ['one','two','three']
for i in str1:
    print(i)

a = [1,2,3,4,5]
print('',[x*10 for x in a]) # [10, 20, 30, 40, 50]

# Ex เราอยากแยกตัวเลข
a = [1,2,3,4,5]
print('',[x for x in a if x%2 == 0]) #แยกเลขคู่ [2, 4]
print('',[x for x in a if x%2 != 0]) #แยกดลขคี่  [1, 3, 5]

[print ('', x*2,sep = ',') for x in a] # test 

#operator list
a = [1,2,3]
b = [4,5,6]
c = a + b ; print (c) #[1, 2, 3, 4, 5, 6]
c = b + a ; print (c) #[4, 5, 6, 1, 2, 3]
d = a*2 ; print(d) #[1, 2, 3, 1, 2, 3]

fruit = ['apple','banana','coconut']
print('banana' in fruit) #True หัดใช้ฟังชัน์ in

a = [0,1,2,3,4,5,6,7,8]
b = a[2:5] ;print(b) # [2, 3, 4] ตัดตัวท้าย แต่ไม่ตัดตัวหน้านะ
print(a[2:]) #[2, 3, 4, 5, 6, 7, 8]
print(a[:7]) #[0, 1, 2, 3, 4, 5, 6] 

# function builtin & LIST

a = [0,1,2,3,4,5,6,7,8,9]
print(len(a)) #นับได้ 10 ตัว 
print(sum(a)) #รวม 45

b = ['abcABCe']
print(len(b)) # นับได้ 1 ตัว 

b = list('abcABCe') ; print(len(b)) # 7 ตัว 

c = [100,400,200,123]
print(max(c)) #max 400
print(min(c)) #min 100

h = [10,11,12,13,14,15,16,17]
print(h)
count1 = 0

for i in range(0,len(h)):
    if h[i]%2 == 0:
        count1 += 1
        print(h[i])
# enumerate (index,value)
g = [108,1009,7,11]
for (i,v) in enumerate(g):
    print(f'{i}-{v}') #(index,value)

#append
a = [1,2,3,4]
a.append(4); print(a) #[1, 2, 3, 4, 4]

# Ex ปีเกิด
constellations = ['ชวด','ฉลู','เถาะ','ขาล','มะโรง',',มะเส็ง','มะเมีย',',มะแม','วอก','ระกา','จอ','กุน']

#year = int(input('ปี พ.ศ.ของคุณคือ:'))
#print('ปีเกิดของคุณ:', constellations[(year+5)%12] )

# List array 2 D
nums = [[1,2,3],[4,5,6]]
print(nums[0]) #1, 2, 3]
print(nums[0][1]) #2
print(len(nums)) #2
print(len(nums[1])) #3

