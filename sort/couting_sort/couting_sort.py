from typing import List


def couting_sort(nums:List[int]) -> List[int]:
    size = max(nums)

    new_nums = [0] * (size  + 1)

    for i in nums:
        new_nums[i] += 1 

    sorted_array = []

    for i in range(size + 1):
        sorted_array.extend([i] * new_nums[i])

    return sorted_array

nums:List[int] = [4, 2, 2, 8, 3, 3, 1]
print(couting_sort(nums))



