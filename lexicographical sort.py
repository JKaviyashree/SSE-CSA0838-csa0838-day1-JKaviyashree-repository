def cs(n,st):
    if n==0:
        return 1
    cnt=0
    for i in range(st,5):
        cnt+=cs(n-1,i)
    return cnt
def cvs(n):
    return cs(n,0)
n=int(input("Enter : "))
print(cvs(n))
