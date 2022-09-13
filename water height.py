def MaxVal(height):
    low=0
    high = len(height)-1
    ans = 0
    while low < high:
        if height[low]<height[high]:
            min_height=height[low]
            min_height_index=low
        else :
            min_height=height[high]
            min_height_index=high
        ans=max(((high-low))*min_height,ans)
        if low+1==min_height_index+1:
            low=low+1
        else:
            high=high-1
    return ans
l=[]
r=int(input("Range : "))
for i in range (r):
    i=int(input("Height : "))
    l.append(i)
print(MaxVal(l))
    
