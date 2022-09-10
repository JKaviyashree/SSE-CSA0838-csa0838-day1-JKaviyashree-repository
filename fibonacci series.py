#Fibonacci series

r=int(input("number : "))
n1=0
n2=1
print("Fibonacci Series : ")
print(n1)
print(n2)
for i in range(1,r+1,1):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
