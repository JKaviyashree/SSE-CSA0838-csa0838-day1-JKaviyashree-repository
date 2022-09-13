import re
s=input("S1 : ")
p=input("S2 : ")
p=r"{}".format(p)
p=re.compile(p)
if p.fullmatch(s):
    print("true")
else:
    print("false")
    
    
