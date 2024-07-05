from openai import OpenAI
client = OpenAI()

# ChatGPT request 관리 함수
def call_chat_gpt():

    # 프롬프트 요청 내용
    request = "저는 32개월 딸 아이 한명과 현재 임신 8주차 아내를 보살피고 있는 가장입니다. " \
              "아빠로써 겪을 심적인 고통과 괴로움을 유머로 승화해서 올릴 트윗을 저를 대신해 작성해주세요." \
              "트윗을 작성할 때 다음 예문을 참고해 주세요. \n\n"

    # 예문
    ex1 = "예문1 : 직장과 육아의 갈림길 속에서 겉은 육아를 선택하려는 듯 보이지만 마음은 이미 직장에 가 있다. \n"
    ex2 = "예문2 : 어느새 육아 퇴근을 직장 퇴근 보다 더 기다리고 있는 웃픈 현실을 마주하다"

    # 요청과 예문 합치기
    content = request + ex1 + ex2

    # chatGPT API 요청 보내기
    res = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=1, # 0으로 하면 너무 formal하며 예문으로 준 글과 거의 비슷하게 작성하기 때문에
                       # 창의적이며 독특한 작성을 위해 1정도 값을 지정해보고 수정한다.
        messages=[
            {
                "role":"system",
                "content":"당신은 매우 긍정적이고, 밝은 성격을 가지고 있습니다. "
                          "시적으로 표현하는 것을 좋아합니다. "
                          "말 끝을 '~하다, ~한다'로 끝맺는 버릇이 있습니다."
            },
            {
                "role":"user",
                "content":content
            }
        ]
    )

    result = res.choices[0].message.content

    return result

