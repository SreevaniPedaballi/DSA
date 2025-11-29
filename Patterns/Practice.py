"""
          *
         * *  
       * * * *  
     * * * * * *  
   * * * * * * * *  
 * * * * * * * * * *  


"""


def pattern(n):
    print("  "*n,end="")
    print("*")
    for row in range(n,0,-1):
        print("  "*(row-1),end=" ")
        print("* "*(n-row+1),end="")
        print("* "*(n-row+1),end=" ")
        print("")

pattern(5)

