class Twitter:

    def __init__(self):
        self.tweets = []
        self.users = {}     

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.addUser(userId)
        tweet = {
            'userId': userId,
            'tweetId': tweetId
        }
        self.tweets.append(tweet)
        
    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        user = self.users[userId]
        ids = user['following']
        ids.add(userId)

        tweetIds = []
        i = len(self.tweets) - 1
        while i >= 0 and len(tweetIds) < 10:
            tweet = self.tweets[i]
            if tweet['userId'] in ids:
                tweetIds.append(tweet['tweetId'])
            i -= 1

        return tweetIds  

    def addUser(self, userId):
        if userId in self.users.keys():
            return self.users[userId]

        self.users[userId] = {
            'followers': set(),
            'following': set()
        }
        return self.users[userId]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.addUser(followerId)
        if followeeId not in self.users:
            self.addUser(followeeId)

        follower = self.users[followerId]
        followee = self.users[followeeId]
        followee['followers'].add(followerId)
        follower['following'].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.addUser(followerId)
        if followeeId not in self.users:
            self.addUser(followeeId)

        follower = self.users[followerId]
        followee = self.users[followeeId]
        print(followee)
        if followerId in followee['followers']:
            followee['followers'].remove(followerId)
        if followeeId in follower['following']:
            follower['following'].remove(followeeId)
        
