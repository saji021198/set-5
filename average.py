p=int(input())
array=list(map(int,input().split()))
sum=0
for i in range(p):
    sum=sum+array[i]
d=sum//p
print(d)
