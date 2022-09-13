def fibonacci(n):
    if(n<=1):
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
s=int(input("Enter the Value : "))
print("Fibonacci Series : ")
for i in range(s):
    print(fibonacci(i))
