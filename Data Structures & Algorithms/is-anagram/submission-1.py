class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_map = {}

        # Count frequencies for s
        for char in s:
            char_map[char] = char_map.get(char, 0) + 1
        
        # Subtract frequencies for t
        for char in t:
            if char not in char_map:
                return False # Found a char not in s1
            char_map[char] -= 1

            if char_map[char] < 0:
                return False # Found more of a char than in s1
                
        # If all values are 0, it's a valid anagram
        return all(count == 0 for count in char_map.values())