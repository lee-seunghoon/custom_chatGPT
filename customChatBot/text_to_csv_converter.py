import pandas as pd
import re

def remove_newlines(text: str) -> str:
    """
    문자열 줄 바꿈 & 연속 공백 삭제
    :param text: 한국어 텍스트 데이터 
    :return: 전처리된 text data 
    """
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r' +', ' ', text)
    return text


def text_to_df(data_fname: str) -> pd.DataFrame:
    """
    텍스트 파일 처리하여 DataFrame으로 전환
    :param data_fname: 처리한 데이터 파일명
    :return: 데이터 프레임 구조로 데이터 재정의
    """

    all_texts = []

    # 파일 가져와서 처리
    with open(data_fname, 'r', encoding='utf-8') as f:

        # txt 파일 내용 문자열로 가져오기
        text = f.read()

        # 줄 바꿈을 기준으로 문자열 분리
        sections = text.split('\n\n')

        # 각 세션에 대해 처리
        for section in sections:
            # 각 섹션 안에 줄바꿈을 기준으로 분리
            lines = section.split('\n')
            # 첫 번재 항목은 타이틀, 유형에 해당함
            text_type = lines[0]
            # 두번째 이후 텍스트는 해당 type의 내용
            content = ' '.join(lines[1:])
            # 추출한 위 정보들 all_texts에 추가
            all_texts.append([text_type, content])

    # df 생성
    df = pd.DataFrame(all_texts, columns=['type', 'text'])
    # 각 contens text 전처리
    df['text'] = df['text'].apply(remove_newlines)

    return df


df = text_to_df('./data/data.txt')
df.to_csv('./data/data.csv', index=False, encoding='utf-8')
