# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
def Count_Steps(num,steps=0):
    if num==0:
        return steps
    num= num//2 if num%2==0 else num-1
    steps +=1
    return Count_Steps(num,steps)
num=8
no_steps=Count_Steps(num)
print(no_steps)
