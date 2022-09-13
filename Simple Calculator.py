print("Perform Calculation of : 1-Addition 2-Subtraction 3-Multiplication 4-Division 5-Modulo 6-Power 7-Floor Dividion")
c=int(input("Choice : "))
n1=int(input("Number 1 : "))
n2=int(input("Number 2 : "))
if c==1:
    print(n1," + ",n2," = ",n1+n2)
elif c==2:
    print(n1," - ",n2," = ",n1-n2)
elif c==3:
    print(n1," * ",n2," = ",n1*n2)
elif c==4:
    print(n1," / ",n2," = ",n1/n2)
elif c==5:
    print(n1," % ",n2," = ",n1%n2)
elif c==6:
    print(n1," ** ",n2," = ",n1**n2)
elif c==7:
    print(n1," // ",n2," = ",n1//n2)
else:
    print("Invalid Input")
