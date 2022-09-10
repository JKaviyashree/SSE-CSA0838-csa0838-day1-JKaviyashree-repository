# count word and characters

s=str(input("Enter string : "))
w=1
c=0
for i in (s):
    c=c+1
    if(i==" "):
        w=w+1
print(w,"Words in given string ",c,"Characters in given string ")
