"""
*
**
***
****
*****
****
***
**
*

"""

def pattern1(n):
    for row in range(n):
        for col in range(row+1):
            print("*",end=" ")
        print("")
def pattern2(n):
    for row in range(n-1,0,-1):
        print("* "*row)
pattern1(5)
pattern2(5)