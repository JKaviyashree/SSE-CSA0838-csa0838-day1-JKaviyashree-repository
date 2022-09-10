# Grade Average Marks

m1=int(input("Mark 1 : "))
m2=int(input("Mark 2 : "))
m3=int(input("Mark 3 : "))
m4=int(input("Mark 4 : "))
m5=int(input("Mark 5 : "))
m=m1+m2+m3+m4+m5
avg=m/5
if(m>=450 and m<=500):
    print("S Grade")
elif(m>=400 and m<450):
    print("A Grade")
elif(m>=350 and m<400):
    print("B Grade")
elif(m>=300 and m<350):
    print("C Grade")
elif(m>=250 and m<300):
    print("D Grade")
elif(m>=200 and m<250):
    print("E Grade")
elif(m>=0 and m<200):
    print("F Grade")
else:
    print("Wrong Input")
print("Total Marks : ",m,"Average : ",avg)

