import math

def reverse_num(n, digits):
    if n % 10 == n:             # base case: 1 digit left
        return n
    
    return (n % 10) * (10 ** (digits)) + reverse_num(n // 10, digits - 1)


n = 2345
digits = int(math.log10(n)) + 1   # number of digits
ans = reverse_num(n, digits - 1)
print(ans)
