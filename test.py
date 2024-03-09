n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
arr1=[]
arr2=[]
for i in numbers:
    if int(i) %2 == 0:
        arr1.append(int(i))
    else:
        arr2.append(int(i))
res = arr1+ arr2
print(*res)
