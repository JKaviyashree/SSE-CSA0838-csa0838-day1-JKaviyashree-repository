def comb(L):      
    for i in range(len(L)):
        for j in range(len(L)):
            for k in range(len(L)):
                if (i!=j and j!=k and i!=k):
                    print(L[i],L[j],L[k])
list=[]
r=int(input("Range : "))
n=0
for i in range (3) :
   m=r%10
   n=n*10+m
   r=r//10
   list.append(m)
comb(list)
