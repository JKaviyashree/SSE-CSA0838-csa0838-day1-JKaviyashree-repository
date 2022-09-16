num=int(input("Enter the Number : "))
tempnum=num
numrev=0
while(num > 0):
    rem = num % 10
    numrev = numrev * 10 + rem
    num = num // 10
print("Reverse of ",tempnum," : ",numrev)

