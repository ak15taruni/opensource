t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    if m<=n:
        print(n-m)
    else:
        print(0)
        
