#Python function sumsquare(l) that takes a nonempty list of integers and returns a list [odd,even], where odd is the sum of squares of all the odd numbers in l and even is the sum of squares of all the even numbers in l

l=[]
a=int(input("Enter the list limit : "))
for i in range(0,a):
    b=int(input("Enter Element : "))
    l.append(b)
print(l)
def sqsum(a):
    odd=0
    even=0
    for i in a :
        if (i%2==0):
            even=even+(i*i)
        else:
            odd=odd+(i*i)
    a=[odd,even]
    return a
print(sqsum(l))
