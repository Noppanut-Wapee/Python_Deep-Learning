'''
def num_layers(n):
	#print(n)
    total = pow(2,n)*(0.0005)
   # f = total
    print(type(total))
    total = print('{f}m'.format(f = total))
    total = str(total)
    print(type(total))
    return total

num_layers(100)
#print(total)
'''

def num_layers(n):
    a = format(pow(2,n)*(0.0005))
    return a+'m' 
    
num_layers(100)


