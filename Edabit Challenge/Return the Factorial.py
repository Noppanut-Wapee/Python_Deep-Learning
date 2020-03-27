#แนวคิค
n = int(input('ใส่เลขที่อยากรู้ค่า Fac:'))

fact = 1

for i in range(1,n+1): 
	fact = fact * i 
	
print ("ค่าของ Fac {n}: คือ: {fact}  ".format(n=n,fact=fact)) 
