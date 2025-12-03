def calc_power(base,power):
    ans=1
    while power >0:
        last=power & 1
        power=power >> 1
        ans =ans * base if last ==1 else ans
        base *=base
    return ans

# base=3
# pow=6

base=5
pow=5
ans=calc_power(base,pow)
print(ans)
