class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1 — sort the array
# Step 2 — loop through each number as the fixed first element
# Step 3 — use two pointers on the REST of the array to find pairs that sum to -nums[i]

        nums.sort()
        result = []
        for i in range(len(nums)):
            # skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    # skip duplicates for l and r
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return result

