n,x,y = map(int,input().split())
m = 0
d = y-n*m
a = x-m
if a!=0 and d%a==0:
    z = d//a
    if 0<=z<=n:
        print("YES")
    else:
        print("NO")
elif a==0 and y==n*x:
    print("YES")
else:
    print("NO")
