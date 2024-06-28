# import sys
# print(sys.path)


class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0 or n==1:
            return n
        
        else: tribonacci(n-1) + tribonacci(n-2) 