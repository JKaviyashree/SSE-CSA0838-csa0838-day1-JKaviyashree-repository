def solve(nums):
   count=0
   n=len(nums)
   for i in range(n):
      for j in range(i+1,n):
         if nums[i] == nums[j]:
            count+=1
   return count
lst=[]
l=int(input("Range : "))
for k in range(l):
    k=int(input("Enter : "))
    lst.append(k)
print(solve(lst))
