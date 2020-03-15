# ความแตกต่างของ Tuple กับ List 
# List ใช้ [] , Tuple ใช้ ()
# List แก้ไขสมาชิกได้ ส่วน Tuple แก้ไขไม่ได้
# List เปลี่ยนแปลงลำดับได้ ส่วน Tuple ไม่ได้
# List นิยมใช้สมาชิกจำนวนมากๆ Tuple ใช่กรณีสมาชิกมีไม่มากนัก

Tuple = (1,2,3) ;print(type(Tuple)) #<class 'tuple'>
List = [1,2,3]

a = tuple(list(List)) ; print(a) # (1, 2, 3)

#การกำหนด Tuple
a = (1,)   ;print(type(a)) # <class 'tuple'>
b = (1) ; print(type(b)) #<class 'int'> เพราะฉะนั้นอย่าลืม , ตัวสุดท้าย


a = (1,2,3) ; b = (4,5,6)
c = a+b ; print(c)
# del a[1] จะ error เพราะ Tuple ลบม่ายยยด้ายยยย


