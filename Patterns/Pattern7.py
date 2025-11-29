"""
7.   *****
      ****
       ***
        **
         *
"""

def pattern(n):
    for row in range(n):
        print(" "*row,end=" ")
        print("*"*(n-row),end=" ")
        print("")
pattern(5)