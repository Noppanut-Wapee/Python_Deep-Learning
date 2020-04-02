def simon_says(lst1, lst2):
    nums = 0
    total = 0 
    print(len(lst1))
    for i in range(len(lst1)):
        if lst1[i] == (lst2[i]+1):
            total += 1
        print(i)
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                nums += 1
                print('2')
    print(total)
    print(nums)
    if nums == 1:
        return print(True)
    elif total == (len(lst1)):
        return print(True)
    else:
        return print(False)


simon_says(
	[1, 1],
	[1, 1]
)

# สั้นๆ 
def simon_says1(lst1, lst2):
  return print(lst1[:-1] == lst2[1:])

simon_says1(
	[1, 1],
	[1, 1]
)


a = [1, 2, 3, 4, 5]
b = [5, 9, 9, 9, 9]

print(a[:-1])
print(b[1:])