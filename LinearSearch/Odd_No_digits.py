import math
def no_digits_count(num):
    count=0
    while num >0:
        count += 1
        num=num//10
    return count

def no_digits_count1(num):
    return int(math.log10(abs(num)))+1 
def get_odd_no_digit_ele(arr):
    if not arr:
        return 0
    res=[]
    for idx in range(len(arr)):
        no_digits=no_digits_count1(arr[idx])
        if no_digits%2!=0:
            res.append(arr[idx])
    return res if res else 0

arr=[123,2345,12,234,23456,234567]
print(arr)
ans=get_odd_no_digit_ele(arr)
print(ans)