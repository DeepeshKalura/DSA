from typing import List

def binary_search(nums:List[int], key:int) ->int:
    i = 0
    n = len(nums) - 1

    while(i < n):
        mid:int = (i + n) // 2

        if(nums[mid] == key):
            return mid 
        elif (nums[mid] > key):
            n = mid - 1
        else:
            i = mid + 1

    return -1



def main() -> None: 
    nums = [1,2,3,4,5]
    k = 4

    index = binary_search(nums, k)

    if(index == -1):
        print("No key does not exit in the binary search")

    else:
        print(f"{nums[index]} exits in this {index} index.")

if __name__ == "__main__":
    main()