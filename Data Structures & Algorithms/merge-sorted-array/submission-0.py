class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1 # points to the largest number of nums1
        p2 = n-1 # points to the largest number of nums2
        p3 = m+n-1 # points to the largest number of array m+n

        while p2 >= 0:
            # num2 at p2 is bigger than num1 at p1
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
            
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1
            p3 -= 1
        

    