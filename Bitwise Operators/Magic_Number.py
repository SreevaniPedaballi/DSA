def magic_number(n):
    base=5
    ans=0
    while n >0:
        last=n&1 # to get last bit of teh number
        n=n >> 1
        ans += last * base
        base =base *5
    return ans
n=10
print(magic_number(n))