def product_of_digits(n):
    if n%10 ==n:#stop recursion when n is single digit.eg 2%10=2
        return n
    return (n%10)*product_of_digits(n//10)

n=1203
ans=product_of_digits(n)
print(ans)