"""
make it 1 
set 0 if 1 exists
set 1 if 1 exists

0->1
1->1

logic (num | ())

eg :
10=1010
ith=2

1010
0010(OR)
------
1010= 10

ith=3

1010
0100
-----
1110=14
"""
def set_ith_bit(num,ith):
    return num|(1 <<(ith-1))

num=10
ith=2
ans=set_ith_bit(num,ith)
print(ans)

ith=3
ans=set_ith_bit(num,ith)
print(ans)