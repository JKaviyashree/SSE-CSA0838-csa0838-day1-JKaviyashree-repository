r=int(input("Enter the Range : "))
s=int(input("Enter the row to find its sum : "))
if(s<=0 or r<=0):
    print("Wrong Input")
elif(s>=r):
    print("Wrong Input")
elif (s <= r ):
    t=0
    for i in range (1,r+1):
        for j in range(0,r-i+1):
            print(" ",end=' ')
        c=1
        for j in range(1,i+1):
            print(' ',c,sep=' ',end=' ')
            c=c*(i-j)//j
            if(i==s):
                t=c+t
        print()
    print("Sum of ",s,"th row :",t+1)
else:
    print("Wrong Input")

