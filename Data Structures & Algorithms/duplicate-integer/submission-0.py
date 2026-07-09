class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        duplicates = False
        for number in nums:
            if number not in seen:
                seen.append(number)
            else:
                duplicates = True

        return duplicates
        