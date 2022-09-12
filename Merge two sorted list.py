# Merge two sorted list

al=[]
bl=[]
ar=int(input("Range of list A : "))
br=int(input("Range of list B : "))
for i in range (ar):
    a=int(input("LA : "))
    al.append(a)
for i in range (br):
    b=int(input("LB : "))
    bl.append(b)
bl.extend(al)
bl.sort()
print(bl)
