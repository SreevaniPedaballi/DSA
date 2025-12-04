import math
def factors(num):
    ans=[]
    for i in range(1,num+1):
        if num%i==0:
            ans.append(i)
    return ans

def factors1(num):
    ans=[]
    for i in range(1,int(math.sqrt(num))+1):
        if num%i==0:
            ans.append(i)
            ans.append(num//i)
    return sorted(ans,reverse=False)



num=20
ans=factors(num)
ans1=factors1(num)
print(ans)
print(ans1)



