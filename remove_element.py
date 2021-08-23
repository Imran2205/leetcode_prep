class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = i
        while j < len(nums):
            if not nums[j] == val:
                nums[i] = nums[j]
                i += 1
            j += 1

        print(nums)