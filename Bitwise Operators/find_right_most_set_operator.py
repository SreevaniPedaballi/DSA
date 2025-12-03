"""
set operator means 1. if we want to find out the right mosrt set operator that is 1 then 

eg: num=12=1100
next get -ve num
in order to get -ve num first we need to get num compliment +1
~num=0011(this is ones compliment)
Add 1
0011
0001 +
-----
0100=4(ans)

"""
def find_right_most_set_operator(num):
    return num & -num

num=12
ans=find_right_most_set_operator(num)
print(ans)