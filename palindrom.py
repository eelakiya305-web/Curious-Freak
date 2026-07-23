class Solution:
    def isPalindrome(self, n):
        original = n
        reverse = 0
        while n > 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n //= 10

        return original == reverse
n=int(input())
ob=Solution()
print(ob.isPalindrome(n))