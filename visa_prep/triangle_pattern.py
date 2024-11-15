n = int(input())
r = 1
for i in range(n):
    for j in range(i+1):
        print(r,end=" ")
        r+=1
    print()
