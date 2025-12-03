# https://leetcode.com/problems/flipping-an-image/description/
# arr=[[1,1,0],[1,0,1],[0,0,0]]
# print(arr)
# for row_idx in range(len(arr)):
#     for col_idx in range(len(arr[row_idx])//2):
#         temp=arr[row_idx][col_idx] 
#         arr[row_idx][col_idx]=(arr[row_idx][len(arr[row_idx])-1-col_idx] ) ^ 1
#         arr[row_idx][len(arr[row_idx])-1-col_idx]=(temp) ^ 1
# print(arr)


arr = [[1,1,0,1],[1,0,1,1],[0,0,0,1]]
print(arr)

for row_idx in range(len(arr)):
    n = len(arr[row_idx])

    # swap + flip
    for col_idx in range(n//2):
        temp = arr[row_idx][col_idx]
        arr[row_idx][col_idx] = arr[row_idx][n - 1 - col_idx] ^ 1
        arr[row_idx][n - 1 - col_idx] = temp ^ 1

    # flip middle element if odd length
    if n % 2 == 1:
        arr[row_idx][n//2] ^= 1

print(arr)
