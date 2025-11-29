"""
*  
*  *  
*  *  *  
*  *  *  *  
*  *  *  *  *  
*  *  *  *  *  * 
"""

def pattern(n):
    for rows in range(n+1):
        for col in range(rows+1):
            print("* ",end=" ")
        print("")
        


pattern(5)