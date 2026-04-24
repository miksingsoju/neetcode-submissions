class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def helper(i):
            # Base cases: if we reach the end exactly, it's 1 way
            if i == n:
                return 1
            # If we overstep, it's 0 ways
            if i > n:
                return 0
            
            # Check if we already have the answer for this step in our cache
            if i in cache:
                return cache[i]
            
            # Calculate: Choice 1 (1 step) + Choice 2 (2 steps)
            cache[i] = helper(i + 1) + helper(i + 2)
            return cache[i]

        return helper(0)