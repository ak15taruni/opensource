v,c = input().split()
if (v=='R' and c=='S' or v=='P' and c=='R' or v=='S' and c=='P'):
    print("Vignesh")
elif(c=='R' and v=='S' or c=='P' and v=='R' or c=='S' and v=='P'):
    print("Charan")
else:
    print("NULL")
