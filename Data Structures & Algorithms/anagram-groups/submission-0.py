class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # This hash map stores the frequency tuple as the key 
        # and the list of anagrams as the value.
        anagram_map = {}
        
        for s in strs:
            # Create a frequency count array of size 26 for 'a'-'z'
            count = [0] * 26
            for char in s:
                # Map 'a' to 0, 'b' to 1, ..., 'z' to 25
                count[ord(char) - ord('a')] += 1
            
            # Tuples are hashable and can be used as dictionary keys
            key = tuple(count)
            
            if key not in anagram_map:
                anagram_map[key] = []
            
            anagram_map[key].append(s)
            
        return list(anagram_map.values())