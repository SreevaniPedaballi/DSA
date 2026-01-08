def sum_of_digits(n):
    if n%10==n:
        return n
    first_digit=n%10
    remaining_digits=n//10
    return first_digit+sum_of_digits(remaining_digits)

n=2345
ans=sum_of_digits(n)
print(ans)