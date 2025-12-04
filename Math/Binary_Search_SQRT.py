def sqrt(n,p):
    s=0
    e=n
    root=0
    while s <=e:
        m= s+(e-s)//2
        if m*m == n:
            root= m
            break
        elif m*m < n:
             s=m+1
             root=m
        else:
            e=m-1
           
    incr=0.1
    for i in range(p):
        while root*root <= n:
            root += incr
        root -=incr
        incr /=10
    return root


print(sqrt(40,3))



