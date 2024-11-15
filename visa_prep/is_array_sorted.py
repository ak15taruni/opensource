n = int(input())
l = list(map(int,input().split()))
is_sorted = True
for i in range(1,len(l)):
    if l[i]<l[i-1]:
        is_sorted = False
        break
if is_sorted:
    print("true")
else:
    print("false")
