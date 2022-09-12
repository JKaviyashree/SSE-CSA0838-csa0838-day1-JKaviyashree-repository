# Happy Number

num=int(input("Enter the Number : "))
def Happynum(n):
  pt=set()
  while n!= 1:
    n = sum(int(i)**2 for i in str(n))
    if n in pt:
      return False
    pt.add(n)
  return True
print(Happynum(num))


