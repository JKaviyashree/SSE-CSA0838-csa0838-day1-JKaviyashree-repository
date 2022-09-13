def phone(digits):
    if len(digits)==0:
        return[]
    char = {2 : " abc" ,3 : "def",4: "ghi",5 : "jkl",6: "mno",7:"pqrst",8:"tuv",9:"wxyz"}
    result=[]
    solve(digits,char,result)
    return result
def solve(digits,char,result,cs="",cl=0):
    if cl==len(digits):
        result.append(cs)
        return
    for i in char[int(digits[cl])]:
        solve(digits,char,result,cs+i,cl+1)
m=input("Enter the number : ")
print(phone(m))
        
    
