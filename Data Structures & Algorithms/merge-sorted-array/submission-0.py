class Solution:
    def merge(self, nums1, m, nums2, n):

        # i → points to the last valid element in nums1
        i = m - 1

        # j → points to the last element in nums2
        j = n - 1

        # k → points to the last position of nums1
        k = m + n - 1

        # Continue until all elements of nums2 are placed
        while j >= 0:

            # If nums1 still has elements
            # AND nums1[i] is greater than nums2[j]
            if i >= 0 and nums1[i] > nums2[j]:

                # Put the bigger element at the end
                nums1[k] = nums1[i]

                # Move i backward
                i -= 1

            else:

                # Put nums2[j] at the current position
                nums1[k] = nums2[j]

                # Move j backward
                j -= 1

            # Move the position where we are placing elements
            k -= 1