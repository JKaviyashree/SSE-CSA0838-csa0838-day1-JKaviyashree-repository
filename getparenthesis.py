def getparen(n):
    result=[]
    parget(n,n,"",result)
    return result
def parget(left,right,temp,result):
    if left == 0 and right == 0 :
        result.append(temp)
        return
    if left > 0:
        parget(left-1,right,temp+'(',result)
    if right > left :
        parget(left,right-1,temp+')',result)
m=int(input("Enter the number : "))
print(getparen(m))
