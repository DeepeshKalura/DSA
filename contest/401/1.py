class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        cycle = 2 * (n - 1)
        remainder = k % cycle
        if remainder < n:
            return remainder
        else:
            return cycle - remainder