class Solution:
    def digitcount(self,n):
        count=0
        temp=n
        while(temp>0):
            digit=temp%10
            if digit!=0 and n%digit==0:
                count+=1
            temp=temp//10
        return count
n=int(input())
ob=Solution()
result=ob.digitcount(n)
print(result)
