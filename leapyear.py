n=int(input("enter a year :"))
if(n%4!=0):
    print("not a leap year")
else:
    if(n%100!=0):
        print(" leap year")
    else:
        if(n%400==0):
            print("leap year")
        else:
            print("it is not a leap year")