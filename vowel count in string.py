s=input("Enter : ")
v=0
for i in s:
    if ( i=='a' or i=='i' or i=='e' or i=='u' or i=='o' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U' ):
        v=v+1
print("Number of vowels in the string : ",v)
