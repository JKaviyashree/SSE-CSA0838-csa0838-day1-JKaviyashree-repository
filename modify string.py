def modifystring(st):
        freq=[0]*26
        n=len(st)
        for i in range(n):
                freq[ord(st[i])-ord('a')]+=1
        for i in range(n):
                add = freq[ord(st[i])-ord('a')]%26
                if (ord(st[i])+add <= ord('z')):
                        st[i]=chr(ord(st[i])+add)
                else :
                        add=(ord(st[i])+add)-(ord('z'))
                        st[i]=chr(ord('a')+add-1)
        print("".join(st))
strl=input("Enter : ")
print("Output : ")
modifystring([i for i in strl])
                           
