num=int(input("Enter the Number : "))
tempnum=num
numrev=0
while(num > 0):
    rem = num % 10
    numrev = numrev * 10 + rem
    num = num // 10
if(numrev == tempnum):
    print("Palindrome")
else:
    print("Not Palindrome")
