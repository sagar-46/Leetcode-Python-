class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = defaultdict(int)

        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1
        double,missing = 0,0
        for num in range(1,n*n + 1):
            if count[num] == 0:
                missing = num
            if count[num] == 2:
                double = num
        return [double,missing]

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        ans = [0,0]
        for row in grid:
            for n in row:
                if n in seen:
                    ans[0] = n
                seen.add(n)
        for n in range(1,len(grid) * len(grid) + 1):
            if n not in seen:
                ans[1] = n
                break
        return ans
