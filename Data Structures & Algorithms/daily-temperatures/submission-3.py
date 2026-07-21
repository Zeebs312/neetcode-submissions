class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] #temp, index

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                Temp, sIndex = stack.pop()
                output[sIndex] = (i - sIndex)
            stack.append([t, i])
        return output

