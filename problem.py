n=int(input("enter a number between 1 to 100 :"))
if(n%2==1):
    print("weird")
else:
    if(2<=n and n<=5):
        print("not weird")
    elif(6<=n and n<=20):
        print("weird")
    else:
        print("not weird")
