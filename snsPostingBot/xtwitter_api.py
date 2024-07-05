import tweepy
import os

# 환경변수에서 X(구 트위터) API 키 가져온다.
consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
bearer_token = os.environ["TWITTER_BEARER_TOKEN"]

# X 트윗 게시 함수
def post_tweet(tweet):
    tweet_client = tweepy.Client(
        bearer_token,
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    tweet_client.create_tweet(text=tweet)
