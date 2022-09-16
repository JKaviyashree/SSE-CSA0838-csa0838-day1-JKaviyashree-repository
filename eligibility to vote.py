a=int(input("Enter the age : "))
if(a<0):
    print("not valid ")
elif(a<=17):
    print("you are eligible to vote after ",18-a," years")
elif(a>=18):
    print("You are eligible to vote ")
else:
    print("invalid input")
