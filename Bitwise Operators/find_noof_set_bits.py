def find_noof_set_bits(num):
    count=0
    while num >0:
        last=num &1
        num=num >> 1
        if last==1:
            count+=1
    return count


def find_noof_set_bits_m2(n):
    count=0
    while n >0:
       count +=1
       n -=(n &-n)
    return count
def find_noof_set_bits_m3(n):
    count=0
    while n >0:
       count +=1
       n = (n&(n-1))
    return count
n=45
print(bin(n))
print(find_noof_set_bits(n))
print(find_noof_set_bits_m2(n))
print(find_noof_set_bits_m3(n))

# Pls note hat n&-n is to get the last setbit of the given number
