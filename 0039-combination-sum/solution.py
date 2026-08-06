class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def pick(i, curr, total):
            curr.append(candidates[i])
            solve(i, curr, total + candidates[i])
            curr.pop()

        def not_pick(i, curr, total):
            solve(i + 1, curr, total)

        def solve(i, curr, total):
            if total == target:
                ans.append(curr[:])
                return
            if i == len(candidates) or total > target:
                return
            pick(i, curr, total)
            not_pick(i, curr, total)

        solve(0, [], 0)
        return ans

        