from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        words = set(wordList)

        if endWord not in words:
            return []

        parents = defaultdict(list)

        level = {beginWord}
        found = False

        while level and not found:

            next_level = set()

            for word in level:
                words.discard(word)

            for word in level:

                for i in range(len(word)):

                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        new_word = word[:i] + ch + word[i+1:]

                        if new_word in words:

                            parents[new_word].append(word)
                            next_level.add(new_word)

                            if new_word == endWord:
                                found = True

            level = next_level

        if not found:
            return []

        ans = []

        def dfs(word, path):

            if word == beginWord:
                ans.append(path[::-1])
                return

            for parent in parents[word]:
                dfs(parent, path + [parent])

        dfs(endWord, [endWord])

        return ans