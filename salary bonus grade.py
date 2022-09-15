g=input("Enter the Grade (A/B) : ")
s=int(input("Salary : $ "))
if (g == 'A' and s <= 10000):
    print("Total Salary : $ ",((s//7)+s))
elif (g == 'A' and s > 10000):
    print("Total Salary : $ ",((s//5)+s))
elif (g == 'B' and s <= 10000):
    print("Total Salary : $ ",((s//12)+s))
elif (g == 'B' and s > 10000):
    print("Total Salary : $ ",((s//10)+s))
else:
    print("Wrong input")
        

    
