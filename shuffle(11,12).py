def shuffle (n11,n12):
    li=[]
    lj=[]
    print("Elements of 11 :")
    for i in range (n11):
        i=int(input("Enter : "))
        li.append(i)
    print("Elements of 11 :")
    for j in range (n12):
        j=int(input("Enter : "))
        lj.append(j)
    l=[]
    l=li+lj
    l.sort()
    print("List : ",l)
n=int(input("Enter the 11 range : "))
m=int(input("Enter the 12 range : "))
shuffle(n,m)


