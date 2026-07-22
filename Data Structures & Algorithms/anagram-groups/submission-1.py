class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # This hash map stores the frequency tuple as the key 
        # and the list of anagrams as the value.
        result = defaultdict(list)
        
        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord('a')] += 1
            
            result[tuple(count)].append(s)

        return list(result.values())