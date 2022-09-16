s=input("Enter the symbol : ")
r=int(input("Enter the range : "))
for i in range (r+1):
    for j in range(i):
        print(s,end=" ")
    print(" ")
