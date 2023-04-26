for i in range(1,5):
    for j in range(i):
        print(i,end="\t")
    print()

for i in range(1, 5):
    for j in range(1,i+1):
        print(j, end="\t")
    print()
print()
for i in range(1, 5):
    for j in range(1,i+1):
        print("*", end="\t")
    print()
print()
for i in range(1,5):
    for j in range(5-i): #(i,5)
        print(i,end="\t")
    print()
print()
for i in range(1,5):
    for j in range(1,5):
        if(j==1 or i==4 or i==j ):
            print("*",end="\t")
        else:
            print(" ",end="\t")
    print()