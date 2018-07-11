class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = sorted(nums1 + nums2)                                          #merge into 1 sorted array
        if len(num) % 2 == 0:   
            return float((num[len(num)//2]+num[(len(num)//2)-1])/2)  #return average of middle 2
                                                                                                #if length is even
        else:
            return float(num[len(num)//2])                                        #simply return middle element by indexing half length if length is odd

