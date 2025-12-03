"""
a%4=0 ans=a
a%4=1 ans=1
a%4=2 ans=a+1
a%4=3 ans=0

eg: find XOR of nos from 0 to 6
0^1^2^3 ^4^5^6
6%4=2 so ans=(a+1)=6+1=7

Q: XOR of all nos between a&b
a=3 
b=9

3 ^4^5^6^7^8^9

formula: xor(b) ^ xor(a-1)

"""

def xor_range(a,b):
    return xor(b)^xor(a-1)

def xor(num):
    if num %4==0:
        return num
    elif num %4==1:
        return 1
    elif num %4==2:
        return num+1
    elif num %4==3:
        return 0
    
a=3
b=9

print(xor_range(a,b))
