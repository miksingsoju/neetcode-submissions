class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return list(sorted(set(nums))) != sorted(nums)