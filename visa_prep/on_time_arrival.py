n = int(input())
l = []
for i in range(0,n):
    l.append(int(input()))
for i in range(0,n):
    if l[i] >=30 and l[i]<=60:
        print("YES")
    else:
        print("NO")
