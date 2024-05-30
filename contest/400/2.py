from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        dc = [0] * (days + 2)

        for m in meetings:
            start, end = m
            dc[start] += 1
            if end + 1 <= days:
                dc[end + 1] -= 1

        om = 0
        fd = 0
        for day in range(1, days + 1):
            om += dc[day]
            if om == 0:
                fd += 1

        return fd

