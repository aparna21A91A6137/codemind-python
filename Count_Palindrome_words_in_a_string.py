s=input()
n=s.split()
count=0
for words in n:
    x=words.upper()
    v=x[::-1]
    if x==v:
        count+=1
print(count)