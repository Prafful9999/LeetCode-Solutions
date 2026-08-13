class Twitter:

    def __init__(self):
        self.follow_map = {}
        self.tweet_map = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweet_map:
            self.tweet_map[userId] = []

        self.tweet_map[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        import heapq

        heap = []

        # User ke followed users + khud
        users = self.follow_map.get(userId, set())
        users = users.copy()
        users.add(userId)

        # Har user ka sirf latest tweet heap mein daalo
        for user in users:
            if user in self.tweet_map:
                index = len(self.tweet_map[user]) - 1
                time, tweetId = self.tweet_map[user][index]

                heapq.heappush(heap, (time, tweetId, user, index))

        ans = []

        # Latest 10 tweets
        while heap and len(ans) < 10:
            time, tweetId, user, index = heapq.heappop(heap)

            ans.append(tweetId)

            # Isi user ka next latest tweet
            index -= 1

            if index >= 0:
                time, tweetId = self.tweet_map[user][index]
                heapq.heappush(heap, (time, tweetId, user, index))

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_map:
            self.follow_map[followerId] = set()

        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map:
            self.follow_map[followerId].discard(followeeId)