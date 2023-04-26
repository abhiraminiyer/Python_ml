# n=int(input("enter a number of items "))
# l=[]
# s=[]
# e={}
# for i in range(n):
#     q=input("enter the item and its price").split()
#     l.append(q[0])
#     s.append(int(q[1]))
# for i in range(len(l)):
#     e[l[i]]=s[i]
# print(e)
# for i in range(n):
#     if(e.get(l[i])):
#         e[l[i]]+=s[i]
#         print(e)
#     else:
#         e[l[i]]=s[i]
# print(e)
# for i in e.keys():
#     print(i,e[i])


from collections import*
n=int(input(" number of items :"))
d={}
for i in range(n):
    item=input("enter the name and rate ").split()
    ip=int(item[-1])
    itn=" ".join(item[:-1])
    if d.get(itn):
        d[itn]+=ip
    else:
        d[itn]=ip
for i in d.keys():
    print(i,d[i])