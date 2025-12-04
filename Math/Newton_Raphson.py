import math
def sqrt(n):
    x=n
    root=0
    while True:
     root=0.5*(x+n/x)
     if abs(root-x) <=0:
        break
     x=root
    return root
print(sqrt(40))

