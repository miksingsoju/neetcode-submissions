class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        highest = 0
        consec = 0
        for x in nums:
            if x == 1:
                consec += 1
                highest = max(highest, consec)

            else:
                consec = 0
        return highest