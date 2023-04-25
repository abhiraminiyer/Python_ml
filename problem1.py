p=input("enter a string: " )
def swapi(l):
    k=""
    for i in l:
        if i.islower():
             k+=i.upper()
        else:
            k+=i.lower()
    return(k)
print(swapi(p))
t=input("enter second name ")
print(swapi(t))