def count_zeros(num,count=0):
    count=count +1 if num%10==0 else count
    if num%10==num:
        return count
    return count_zeros(num//10,count)

num=2900900
ans=count_zeros(num,0)
print(ans)