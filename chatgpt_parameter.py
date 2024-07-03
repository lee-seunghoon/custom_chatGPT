import os
import openai

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY # 환경변수에서 API key 값 가져오기

"""
파라미터 설명
"""

res = openai.chat.completions.create(

    # model 모델 선정 가능
    # gpt-3.5-turbo / gpt-3.5-turbo-16k
    # gpt-4 /  gpt-4-32k
    model="gpt-3.5-turbo",


    # messages -> role, content
    # role :
    #     - system : 주로 메세지 시작 부분에 세팅해서 작동 설정
    #     - user : 일반 사용자로서 글쓰기, 지시, 질문의 내용 담는다.
    #     - assingment : 과거 챗gpt의 출력 문장 or 예시를 줄 때 활용
    messages=[
        {
            "role":"system",
            "content":"당신은 사회복지학과 교수입니다."
        },
        {
            "role":"user",
            "content":"능동적 복지에 대한 개념에 대해 알려주세요"
         },
        {
            "role":"assistant",
            "content":"능동적 복지란 재활가능한 복지를 의미한다."
        },
        {
            "role":"user",
            "content":"시험을 준비하고 있는 학생들이 주관식 시험문제를 대비하는 데 도움이 되는 핵심 내용을 정리해주세요"
        }
    ],

    # 참고로 temperature 와 top_p  매개변수는 함께 사용하지 않는 게 좋다.

    # temperature(0-2) -> 생성되는 텍스트의 창의성과 무작위성을 설정
    # 값이 낮아질수록 더 진지하고 실용적인 답변을 생성
    # 값이 올라갈수록 더 창의적으로 무작위적인 답변 생성(일반적인 답변과 멀어짐)
    temperatue=0,

    # top_p -> 문장의 일관성과 다양성 조절
    # 값이 낮을수록 이어서 생성되는 단어의 다양성이 줄어들고
    # 일반적으로 예상할 수 있는 내용의 답변이 생성된다.
    # 반대로 높을수록 다양한 단어를 사용하여 문장의 선택 범위가 넓어진다.
    # 같은 질문이어도 이 매개변수 값에 따라 다른 답변을 생성한다.
    top_p = 1,

    # n -> 답변의 개수를 정할 수 있는 매개변수
    n = 2,

    # stream -> 응답을 실시간으로 받을지 한 번에 받을지에 대한 여부
    # true -> 실시간 답변 받기
    # false -> 한번에 받기
    stream=True,

    # stop -> 리스트로 키워드를 지정할 수 있으며, 해당 키워드가 들어간 문자열 나오면
    #         출력을 중지하게끔 만드는 매개변수
    stop= ["이상원 교수", "핀란드 복지"],

    # max_tokens
    # 챗gpt 답변 길이 제어
    # 최대 토큰 수 == (입력 문장의 토큰 수 + 출력 문장의 토큰 수)
    # 설정한 토큰 수에 도달하면 답변 중간에라도 중지
    # gpt-3.5-turbo 의 최대 토큰 수 : 4,096
    # gpt-4 의 최대 토큰 수 : 8,192

    # 이 변수를 활용하여
    # 1. 과도한 길이의 텍스트 생성을 방지
    # 2. 토큰의 대량 소비로 고액 청구 방지
    # 3. 너무 긴 출력은 쓸 데 없는 내용을 수반할 수 있기에 품질 개선
    max_tokens=5000,

    # presence_penalty
    # 같은 표현이나 문구를 피하고 새로운 단어, 새로운 주젤를 더 많이 사용하는 경향
    # 값이 높을수록 기존 사용했던 단어나 문구는 피한다.
    # 그리고 새로운 주제가 더 많이 등장할 가능성 높다.
    presence_penalty= 1,

    # frequency_penalty
    # 위와 마찬가지로 단어나 문구를 자주 반복되는 것을 제어하는 변수
    # 값이 높을수록 새로운 화제의 답변을 기도할 수 있다.
     frequency_penalty=1,

    # logit_bias
    # 토큰 ID를 활용하여 해당 토큰의 단어나 문구가 답변에 적용되는
    # 확률과 비율을 조정하는 역할 감당
    logit_bias='012DG3' # 예시

    # user
    # 실제 이용자 모니터링 용도
    # 해시값으로 대부분 설정하며, 사용자 고유 식별 기능 담당
    # 고객 ID의 해시값을 사용하거나, 세션ID를 임시로 사용해서 구분 가능

)

result = res.choices[0].message.content
print(result)
