r=int(input("Enter the range of array : "))
l=[]
sum=0
for i in range (r):
    i=int(input("Enter : "))
    l.append(i)
for i in l:
    sum=sum+i
print("Mean : ",sum//r)
for i in range (0,r):
    for j in range (i+1,r):
        if(l[i]==l[j]):
            for k in range (j,r-1):
                l[k]=l[k+1]
        else:
            continue
    for i in range(0,r-1):
        for j in range(i+1,r):
            if(l[i]>l[j]):
                temp=l[j]
                l[j]=l[i]
                l[i]=temp
for i in range(r):
    print(l[i])
if(r%2==0):
    print("Median : ",l[(r+1)//2])
else:
    print("Median : ",l[((r+1)//2)-1])
print("Mode : ")
for i in range(r):
    if(l.count(i)>1):
        print(l[i])

        
