# Happy Number

num=int(input("num : "))
s=0
a=list(num)
for i in (a):
    a=i*i
    s=a+s
if(s == 1):
    print("Happy number")
else:
    print("Not Happy Number")
