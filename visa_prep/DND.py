n,m=map(int,input().split())
l = list(map(int,input().split()))
s1,s2 = 0,0
for i in range(n):
    if l[i]%m==0:
        s1+=l[i]
    else:
        s2+=l[i]
print(s1-s2)
