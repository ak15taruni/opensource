n = int(input())
x = list(map(int,input().split()))
b = []
for i in range(n):
    l = sum(x[:i])
    r = sum(x[i+1:])
    b.append(abs(l-r))
print(" ".join(map(str,b)))
