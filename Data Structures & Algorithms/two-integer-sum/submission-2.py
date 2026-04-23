class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i = 0
        # j = i + 1
        # # nums=[4,5,6]
        # # target=10
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             result = [i, j]
        #             return result

        # {val, index}
        my_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in my_map:
                return [my_map[diff], i]
            my_map[n] = i
            
