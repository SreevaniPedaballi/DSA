
"""
Q is 36 is prime?
In order to answer this ,we need to check whether the 36 has more than 2 divisors
 (other than 1 and 36 so check from number 2)

 2*18
 3*12
 4*9

 6*6

 9*4
 12*3
 18*2

 here the facors are repeating after 6*6 so wwe need to conser the logic like 2 and squrt of 36

 c=2
 c*c < num
"""
def is_prime(num):
    if num <=1:
        return False
    c=2
    while (c*c <=num):
        if num%c==0:
            return False
        c +=1
    return True

for num in range(1,21):
    ans=is_prime(num)
    print(f"{num} - {ans}")