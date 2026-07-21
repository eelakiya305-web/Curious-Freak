class SOlution:
    def primenumber(self,n):
        if n<=0:
            return False
        i=2
        while i*i<=n:
            if n%i==0:
                return False
            i+=1
        return True
n=int(input())
ob=SOlution()
print(ob.primenumber(n))