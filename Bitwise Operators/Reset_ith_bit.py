"""
set 1->0
set 0->0

logic num & (~(1<<ith-1))

eg:
num=10
ith=2


1010
1101(AND)
-----
1000=8
(ans)=8

ith=4

1010
0111(AND)
----------
0010=2

ans=2

"""
def rest_ith_bit(num,ith):
    return num &(~(1<<(ith-1)))


num=10
ith=2
ans=rest_ith_bit(num,ith)
print(ans)

num=10
ith=4
ans=rest_ith_bit(num,ith)
print(ans)