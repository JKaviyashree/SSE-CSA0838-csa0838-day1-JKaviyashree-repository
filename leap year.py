y=int(input("Year : "))
if(y<=0):
    print("Invalid input")
elif(y%400==0 or y%4==0):
    print(y," Leap Year ") 
else :
    print(y," Not Leap Year")
    d=y%4
    t=y-d
    print("Leap Year : ",t)
