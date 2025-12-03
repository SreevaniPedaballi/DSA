def find_unique_2(nums):
    unique=0
    for num in nums:
        """
        num ^ num(that is same num XOR with same )=0
        num ^ 0=num
        in below logic num ^ with same num so it will be zero for same numbers and the unique elemeent alone will left
        """
        unique ^= num
    return unique

# arr=[2,3,5,3,2]
# ans=find_unique(arr)
# print(ans)




    

def find_unique(arr):
    result = 0
    for i in range(32):  # check each bit position
        count = 0
        for num in arr:
            if (num >> i) & 1:  # check if i-th bit is 1
                count += 1
        if count % 3 != 0:  # bit belongs to unique number
            result |= (1 << i)  # set the bit in result

    # Handle negative numbers
    if result >= 2**31:
        result -= 2**32

    return result

arr = [2, 2, 3, 2]
print(find_unique(arr))  # Output: 3
