class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lastSeen={}

        for i in range(len(nums)):

            if nums[i] in lastSeen:
                if i - lastSeen[nums[i]] <=k:
                    return True

            lastSeen[nums[i]]=i
        return False
