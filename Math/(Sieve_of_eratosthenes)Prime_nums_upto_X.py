""" 
Sieve of Eratosthenes :
======================
Step 1:

Create a list from 2 to N.
All numbers are “unmarked” initially (assume prime).

Step 2:

Start with 2 (the first prime).
Cross out all its multiples: 4, 6, 8, 10, 12…

Step 3:

Move to the next unmarked number → 3 (prime).
Cross out its multiples: 6, 9, 12, 15, 18…

Step 4:

Next unmarked number → 5 (prime).
Cross out its multiples: 10, 15, 20, 25…

Step 5:

Stop when the current number squared is > N
(i.e., stop at √N)

Step 6:

Remaining unmarked numbers are all primes.
Time complexity: O(N*log(log N))

"""
def sieve_of_eratosthenes(n):
    prime=[True]*(n+1)
    prime[0],prime[1]=False,False

    p=2
    while p*p <=n:
        if prime[p]:
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    ans=[i for i in range(n+1) if prime[i]]
    print(ans)

sieve_of_eratosthenes(20)
