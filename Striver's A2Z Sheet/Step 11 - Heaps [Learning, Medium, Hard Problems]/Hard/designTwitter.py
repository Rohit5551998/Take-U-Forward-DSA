# mypy: disable-error-code="empty-body"
# QUESTION: Design Twitter
# Design a simplified version of Twitter where users can post tweets, follow/unfollow
# another user, and see the 10 most recent tweets in their news feed. Implement:
#   - postTweet(userId, tweetId): compose a new tweet
#   - getNewsFeed(userId): return the 10 most recent tweet ids in the user's news
#     feed, ordered most-recent first. Feed items are posted by the user or the
#     users they follow.
#   - follow(followerId, followeeId): follower follows followee
#   - unfollow(followerId, followeeId): follower unfollows followee
#
# Example 1:
# Input:
#   postTweet(1, 5); getNewsFeed(1); follow(1, 2); postTweet(2, 6);
#   getNewsFeed(1); unfollow(1, 2); getNewsFeed(1)
# Output: [5]; [6, 5]; [5]
# Explanation: After following user 2, user 1's feed merges both users' tweets by
# recency; after unfollowing, only user 1's own tweets remain.
#
# Constraints:
# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 10^4
# At most 3 * 10^4 calls total to the four methods


"""
#Brute Force:
1.
TC -> O(), SC -> O()

#Better Approach:
1.
TC -> O(), SC -> O()

#Optimal Approach:
1.
TC -> O(), SC -> O()

#KEY INSIGHT:
-
"""

from typing import List


class Twitter:
    def __init__(self) -> None:
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        pass

    def getNewsFeed(self, userId: int) -> List[int]:
        pass

    def follow(self, followerId: int, followeeId: int) -> None:
        pass

    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass


# if __name__ == "__main__":
#     tw = Twitter()
#     tw.postTweet(1, 5)
#     print(tw.getNewsFeed(1))
#     tw.follow(1, 2)
#     tw.postTweet(2, 6)
#     print(tw.getNewsFeed(1))
