# Sum of n number

sn=int(input("Starting Number range : "))
en=int(input("Ending Number range : "))
s=0
for i in range (sn,en+1,1):
    s=s+i
print("Sum of numbers : ",s)
