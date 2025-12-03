def find_ith_bit(num,ith):
    return num & (1 << (ith-1))
num=10
ith=2
ans=find_ith_bit(num,ith)
print(ans)