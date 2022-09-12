"""A party has been organised on a cruise. The party is organised for a limited time (T). The
number of guests entering (E[i]) and leaving (L[i]) the party at every hour is represented as
elements of the array. The task is to find the maximum number of guests present on the cruise 
at any given instance within T hours. """
E=[]
L=[]
T = int(input("Range T : "))
for i in range(T):
    e=int(input("E : "))
    E.append(e)
for i in range(T):
    l=int(input("L : "))
    L.append(l)
Sum=0
Max=0
for i in range(T):
    Sum+=E[i]-L[i]
    Max=max(Sum,Max)
print("output", Max)
