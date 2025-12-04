"""
The Euclidean Algorithm is the fastest and simplest method to find the GCD (HCF) of two numbers.

It works using the rule:

GCD(a, b) = GCD(b, a % b)
(Repeat until remainder becomes 0)

HCF = Highest Common Factor
GCD = Greatest Common Divisor

Find the HCF/GCD of 12 and 18.

Factors of 12 → 1, 2, 3, 4, 6, 12

Factors of 18 → 1, 2, 3, 6, 9, 18

Common factors → 1, 2, 3, 6
Largest → 6

So:

HCF(12,18) = 6

GCD(12,18) = 6
"""

def gcd(a,b):
    while b >0:
        a,b=b,a%b
    return a

def gcd_rec(a,b):
    if b==0:
        return a
    return gcd_rec(b,a%b)
ans=gcd(48,18)
print(ans)

ans1=gcd_rec(48,20)
print(ans1)
