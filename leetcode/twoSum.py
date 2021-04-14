# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    complement = dict()
    for i in range(len(nums)):
        num = nums[i]
        comp = target - num
        if num in complement:
            return(complement[num], i)
        else:
            complement[comp] = i


print(twoSum(nums=[2, 7, 11, 15], target=9))
