class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for number in nums:
            map[number] = map.get(number, 0) + 1

        bucket = [[] for i in range(len(nums) + 1)]
        for num, count in map.items():
            bucket[count].append(num)
    
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result