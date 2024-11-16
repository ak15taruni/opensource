a = int(input())
l = [[12,1,2],[3,4,5],[6,7,8],[9,10,11]]
if a in l[0]:
    print("Winter")
elif a in l[1]:
    print("Spring")
elif a in l[2]:
    print("Summer")
elif a in l[3]:
    print("Autumn")
else:
    print("Invalid")
