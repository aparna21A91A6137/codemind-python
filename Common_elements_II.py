m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(len(a)):
    if a[i] not in b:
        c.append(a[i])
for i in range(len(b)):
    if b[i] not in a:
        c.append(b[i])
print(*c)