class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for r in range(1,len(nums)):
          if nums[r]!=nums[r-1]:
            nums[l]=nums[r]
            l+=1
        return l


     #Another Approach:   
        '''# If the array is empty
        if len(nums) == 0:
            return 0

        # i points to the position of the last unique element
        i = 0

        # j starts from the second element
        for j in range(1, len(nums)):

            # If current element is different
            # from the last unique element
            if nums[j] != nums[i]:

                # Move i to the next position
                i += 1

                # Put the new unique element at nums[i]
                nums[i] = nums[j]

        # Number of unique elements = i + 1
        return i + 1'''