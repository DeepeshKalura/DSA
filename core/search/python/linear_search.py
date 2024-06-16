from typing import List


def linear_search(nums:List[int], key:int )-> int:
    
    for i, value in enumerate(nums):
        if(value == key):
            return i 
    return -1 


def main() -> None: 
    nums = [1,2,3,4,5]
    k = 4

    index = linear_search(nums, k)

    if(index == -1):
        print("No key does not exit in the binary search")

    else:
        print(f"{nums[index]} exits in this {index} index.")

if __name__ == "__main__":
    main()