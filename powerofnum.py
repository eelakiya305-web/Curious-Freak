class Solution:
    def power(self,n):
        temp=n
        rev=0
        while(temp>0):
            digit=temp%10
            rev=rev*10+digit
            temp=temp//10
        return n**rev
n=int(input())
ob=Solution()
print(ob.power(n))