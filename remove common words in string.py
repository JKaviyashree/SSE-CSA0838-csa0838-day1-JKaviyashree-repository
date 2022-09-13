'''Python program to remove words that are common in two Strings
Given two strings S1 and S2, representing sentences, the task is to print both sentences after 
removing all words which are present in both sentences '''

def remove(str1,str2):
    wc={}
    for w in str1.split():
        wc[w]=wc.get(w,0)+1
    for w in str2.split():
        wc[w]=wc.get(w,0)+1
    return [w for w in wc if wc[w] == 1]
sa=input("S1 : ")
sb=input("S2 : ")
print(remove(sa,sb))
