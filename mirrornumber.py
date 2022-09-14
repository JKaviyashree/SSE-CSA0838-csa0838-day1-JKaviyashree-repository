num = int(input("The number to be mirror: "))
mirnum = 0
while(num > 0):
 Reminder = num %10
 mirnum = (mirnum *10) + Reminder
 num = num //10
print("mirror of the provided number is : ", mirnum)
