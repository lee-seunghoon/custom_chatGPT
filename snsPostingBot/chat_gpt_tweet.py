import gpt_api
import xtwitter_api

# 챗GPT에서 생성한 tweet 내용 가져오기
gpt_tweet = gpt_api.call_chat_gpt()

# gpt에서 어떤 내용으로 생성했는지 확인하기
print(gpt_tweet)

# X에 트윗 게시하기
xtwitter_api.post_tweet(gpt_tweet)
