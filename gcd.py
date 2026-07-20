class Solution:
    def gcd(self,a,b):
        while(b!=0):
            a,b=b,a%b
        return a
a=int(input())
b=int(input())
ob=Solution()
print(ob.gcd(a,b))