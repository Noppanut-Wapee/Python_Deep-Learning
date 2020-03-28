'''
count_ones(0) ➞ 0

count_ones(100) ➞ 3

count_ones(999) ➞ 8

format(5, "b")
'101'
int("101", 2)
5
'''



def count_ones(num):
    a = format(num,'b');sum = 0
    for i in range(0,len(a)):
        sum += int(a[i])
    return sum



count_ones(999)

#โคตรสั้น 555
def count_ones(num):
	return bin(num).count('1')