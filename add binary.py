a= int(input("Enter a: "))
b= int(input("Enter b: "))

a = str(a)
b = str(b)
iSum = int(a,2) + int(b,2)
bSum = bin(iSum)

print("Result = ",bSum)
