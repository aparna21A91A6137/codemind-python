a,b=map(int,input().split())
gcd=0
lcm=0
i=1
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        gcd=i
    i=i+1
lcm=(a*b)//gcd
print(lcm)