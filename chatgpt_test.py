import os
import openai

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY # 환경변수에서 API key 값 가져오기

res = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"user",
         "content":"python에 대해 예제 없이 핵심만 간략히 알려주세요"
         }
    ]
)
result = res.choices[0].message.content
print(result)
