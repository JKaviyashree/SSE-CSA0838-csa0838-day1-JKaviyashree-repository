# << 1 >> 10.9.2022

def isomorphic(str1,str2):
    if (len(str1)!=len(str2)):
        return False
    else:
        mp1,mp2={},{}
        for i in range (len(str1)):
            ch1,ch2=str1[i],str2 [i]
            if ch1 not in mp1:
                mp1[ch1]=ch2
            if ch2 not in mp2:
                mp2[ch2]=ch1
            if mp1[ch1]!=ch2 or mp2[ch2]!=ch1:
                return False
    return True
s1=input("S : ")
s2=input("T : ")
print(isomorphic(s1,s2))
