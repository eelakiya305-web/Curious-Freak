class Solution:
    def last_Digit(self,a,b):
        if b=="0":
            return 1
        
        last_digit_a=int(a[-1])

        rem=0
        for i in b:
            rem=(rem*10+int(i))%4

            if rem==0:
                rem=4
        return pow(last_digit_a,rem)
ob=Solution()
print(ob.last_Digit("8","3"))