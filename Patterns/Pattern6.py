"""
6.       *
        **
       ***
      ****
     *****

"""

def pattern1(n):
    for row in range(n,0,-1):
        print((" "*row),end="")
        for col in range(n-row+1):
            print("*",end="")
        print("")

def pattern2(n):
    for row in range(n,0,-1):
        print(("  "*row),end="")
        for col in range(n-row+1):
            print("* ",end="")
        print("")
pattern1(5)
pattern2(5)
