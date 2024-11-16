m = input().strip()
if m.isdigit() and len(m)==10 and sum(map(int,m))>0:
    print("Correct")
elif m.startswith("+") and " " in m:
    a = m.split()
    if len(a[0])==3 and a[0][1:].isdigit() and len(a[1])==10 and a[1].isdigit() and sum(map(int,a[1]))>0:
        print("Correct")
    else:
        print("Incorrect")
else:
    print("Incorrect")
   
