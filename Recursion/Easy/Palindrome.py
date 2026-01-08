import math
def reverse(n,digits):
    if n%10==n:
        return n
    return (n%10)*(10**digits)+reverse(n//10,digits-1)

n=12321
digits=int(math.log10(n))+1
r_n=reverse(n,digits-1)
ans =True if n==r_n else False
# print(ans)


def palindrome(n,s,e):
    if s>=e:
        return True
    return n[s]==n[e] and palindrome(n,s+1,e-1)

ip="1233210"
s=0
e=len(ip)-1
ans=palindrome(ip,s,e)
print(ans)
