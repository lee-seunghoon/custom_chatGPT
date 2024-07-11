import pandas as pd
import tiktoken
from openai import OpenAI
from typing import List
import os

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=OPENAI_API_KEY)

# 임베딩 매게변수
embedding_model = "text-embedding-3-small"  # 1,000 토큰당 $0.00002
embedding_encoding = "cl100k_base"  # GPT-3.5 , GPT-4 경우 cl100k_base 지정 추천
max_tokens = 1500

# 데이터 가져온 후 column 변경
df = pd.read_csv("data/data.csv")
df.columns = ['title', 'text']

# tokenizer setting
tokenizer = tiktoken.get_encoding(embedding_encoding)

# 토큰 개수를 새로운 컬럼에 추가하기
df['n_tokens'] = df.text.apply(lambda x: len(tokenizer.encode(x)))


def split_into_tokens(text_data: str, each_sentenc_max_tokens=500) -> List[str]:
    """
    텍스트를 최대 토큰 수로 나누고 재정의
    :param text: 텍스트 데이터
    :param max_tokens: 최대 토큰 수
    :return:
    """

    # 텍스트를 문장별로 나누어 각 문장의 토큰 개수 구하기
    sentences = text_data.split(".")
    n_tokens = [len(tokenizer.encode(" " + sentence)) for sentence in sentences]

    chunks = []
    tokens_so_far = 0
    chunk = []

    # 각 문장의 토큰 결합하는데 토큰 개수를 같이 판별하여 최대 토큰 개수가 넘지 않는 선에서 결합하기
    for sentence, n_token in zip(sentences, n_tokens):

        # 지금까지 토큰 수와 현재 문장의 토큰 수를 합한 값이 최대 토큰 수를 초과하면
        # 해당 데이터 청크까지 청크 리스트에 추가
        # 청크 및 토큰 수 재설정
        if tokens_so_far + n_token > each_sentenc_max_tokens:
            chunks.append('.'.join(chunk)+".")
            chunk = [] # => chunk를 다시 비어있는 리스트로 / 최대 토큰 수를 넘어갔기 때문에
            tokens_so_far = 0

        # 현재 문장의 토큰 수가 최대 토큰 수보다 클 경우
        # 다음 문장으로 넘어감
        if n_token > each_sentenc_max_tokens:
            continue

        # 그렇지 않다면 문장을 chunk 리스트에 추가
        # 토큰 수를 합계에 추가
        chunk.append(sentence)
        tokens_so_far += n_token + 1

    # 마지막 chunk 리스트에 데이터가 있다면
    # 이 데이터를 chunks 리스트에 추가
    if chunk:
        chunks.append('.'.join(chunk)+".")

    return chunks


# 축약된 텍스트 저장하기 위한 리스트
shortened = []

# 데이터 프레임 각 행마다 루프 처리
for row in df.iterrows():

    text = row[1]['text']
    token_num = row[1]['n_tokens']

    # text가 None 값인 경우 다음 행으로 넘어감
    if text is None:
        continue

    # 토큰 수가 최대 토큰 수보다 큰 경우,
    # 텍스트 데이터를 shortened 리스트에 축약된 결과로 추가
    if token_num > max_tokens:
        shortened.append(split_into_tokens(text))

    # 그 외 경우 텍스트를 그대로 shortened 리스트에 추가
    else:
        shortened.append(text)

# 축양된 데이터 리스트를 기반으로 새로운 데이터 프레임 생성
# column name == text  지정
df = pd.DataFrame(shortened, columns=['text'])

# 각 text의 토큰 수를 계산해서 새로운 열 이름을 text로 지정
df['n_tokens'] = df['text'].apply(lambda x: len(tokenizer.encode(x)))

# text column 값에 embedding 하는 함수
def get_embedding(processed_text: str, model):
    use_text = processed_text.replace("\n", " ")
    result = client.embeddings.create(input=[use_text], model=model).data[0].embedding

    return result


# 기존 만들어 놓은 전처리된 텍스트 활용하여 임베딩 값 반영 후 csv 저장
df['embeddings'] = df['text'].apply(lambda x: get_embedding(x, embedding_model))
df.to_csv("data/embedding_data.csv", index=False)
