"""
8.      *
       ***
      *****
     *******
    *********
"""

def pattern(n):
    for row in range(n,0,-1):
        print(" "*(row-1),end="")
        print("*"*(n-row+1),end="")
        print("*"*(n-row),end="")
        print("")
        
pattern(5)