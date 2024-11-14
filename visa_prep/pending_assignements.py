x,y,z = map(int,input().split())
t = x*y
maxi = z*24*60
if t<=maxi:
    print("YES")
else:
    print("NO")
