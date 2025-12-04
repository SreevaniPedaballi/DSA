"""
✅ LCM — Least Common Multiple

👉 The smallest positive number that is divisible by both numbers.

📘 Example: LCM of 12 and 18

Multiples of 12:
12, 24, 36, 48, 60, 72, …

Multiples of 18:
18, 36, 54, 72, …

Common multiples → 36, 72, ...

The smallest common multiple = 36

👉 So LCM(12, 18) = 36
"""
def hcf_or_gcd(a,b):
    while b>0:
        a,b=b,a%b
    
    return a
def lcm(a,b):
    return a*b//hcf_or_gcd(a,b)
a=2
b=7
print(lcm(a,b))
