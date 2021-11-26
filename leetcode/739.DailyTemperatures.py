class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0 for _ in range(len(temperatures))]
        idx = 0
        for curr in temperatures:            
            while stack and temperatures[stack[-1]] < curr:
                before = stack.pop()
                answer[before] = idx - before
            
            stack.append(idx)
            idx += 1
        return answer
                    