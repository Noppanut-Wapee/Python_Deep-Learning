list2 = list([1,2,3,4,5])

def find_even_nums(num):
    if num%2 == 0:
        num = num
    else:
        num = num-1
    sum = list(range(1,int(num*0.5+1)))

    for i in range(1,int(num*0.5+1)):
        sum[i-1] = int(i*2)
        
    return sum
        
find_even_nums(21)

#สั้นๆ
def find_even_nums(num):
	return [ x for x in range(2,num+1,2)]
