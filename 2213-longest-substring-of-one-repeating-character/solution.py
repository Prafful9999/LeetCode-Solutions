class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:

        n = len(s)

        # tree[node] =
        # [left_char, right_char, prefix, suffix, best, length]
        tree = [["", "", 0, 0, 0, 0] for _ in range(4 * n)]

        def build(node, l, r):
            if l == r:
                tree[node] = [s[l], s[l], 1, 1, 1, 1]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(node)

        def merge(node):
            left = tree[node * 2]
            right = tree[node * 2 + 1]

            # first and last character
            left_char = left[0]
            right_char = right[1]

            # total length
            length = left[5] + right[5]

            # initially prefix and suffix
            prefix = left[2]
            suffix = right[3]

            # best answer from either side
            best = max(left[4], right[4])

            # Boundary characters same hain
            if left[1] == right[0]:

                # substring crossing the boundary
                best = max(best, left[3] + right[2])

                # left pura same character ka hai
                if left[2] == left[5]:
                    prefix = left[5] + right[2]

                # right pura same character ka hai
                if right[3] == right[5]:
                    suffix = right[5] + left[3]

            tree[node] = [
                left_char,
                right_char,
                prefix,
                suffix,
                best,
                length
            ]

        def update(node, l, r, idx, ch):

            if l == r:
                tree[node] = [ch, ch, 1, 1, 1, 1]
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)

            merge(node)

        # Build segment tree
        build(1, 0, n - 1)

        ans = []

        # Process every query
        for i in range(len(queryIndices)):

            idx = queryIndices[i]
            ch = queryCharacters[i]

            update(1, 0, n - 1, idx, ch)

            # tree[1][4] = longest repeating substring
            ans.append(tree[1][4])

        return ans