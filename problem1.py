l=input("enter a string: " )
k=""
for i in l:
    if i.islower():
        k+=i.upper()
    else:
        k+=i.lower()
print(k)