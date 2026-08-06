class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        words = set(wordList)

        if endWord not in words:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, length = q.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":

                    new_word = word[:i] + ch + word[i+1:]

                    if new_word in words:
                        q.append((new_word, length + 1))
                        words.remove(new_word)

        return 0
                    

                        

                    


            

        
        