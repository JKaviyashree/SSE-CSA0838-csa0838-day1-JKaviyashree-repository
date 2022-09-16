print("Perform Calculation of : 1-Power 2-Addition 3-Subtraction 4-Multiplication 5-Division")
c=int(input("Choice : "))
n1=int(input("Number 1 : "))
n2=int(input("Number 2 : "))
if c==2:
    print(n1," + ",n2," = ",n1+n2)
elif c==3:
    print(n1," - ",n2," = ",n1-n2)
elif c==4:
    print(n1," * ",n2," = ",n1*n2)
elif c==5:
    print(n1," // ",n2," = ",n1/n2)
elif c==1:
    print(n1," ** ",n2," = ",n1**n2)
else:
    print("Invalid Input")
