import math

def get_num_digits(num,base):
 return int(math.log(num)/math.log(base))+1

num=10
base=2
ans=get_num_digits(num,base)
print(ans)