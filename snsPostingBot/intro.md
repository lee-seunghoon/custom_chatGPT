# SNS 포스팅 자동 생성 봇 만들기

### 목표 : 챗GPT 활용하여 글을 자동 생성 후 X(구 트위터)에 게시하는 봇을 만들자

<br>

#### point1 - 게시물 생성 봇 생성 경험
#### point2 - 용도에 따른 다양한 봇 경험
#### point3 - 게시물 생성 봇 개발 경험

<br>

#### 자동 생성 봇의 다양한 예

- 각 지역 일기예보 정보 전달
- 철도 운행 상황 게시
- 주식 현황 및 뉴스 게시
- 사용자에게 자동으로 답글 보내거나 팔로우 하기 까지 고급 기능도 등장

<br>

#### 개발 흐름
1. X(구 트위터) 계정 준비 및 API 키 생성
2. ChatGPT 자동생성 프로그램 코딩
3. X(구 트위터) API 활용하여 자동 생성된 글 자동 게시 프로그램 코딩

<br>

#### 특별한 시도

- 특별한 **문체**를 갖기 위해 기존 나의 글을 예문으로 학습시킨다
- 예문을 학습시키는 방법으로
    1. 제로샷 - 참고 사례(예문) 주어지지지 않는 경우
    2. 원샷 - 참고 사례(예문) 1개만 주어지는 경우
    3. 퓨샷 - 참고 사례(예문) 몇가지 주어지는 경우
    
<br>

퓨샷 학습 데이터 예시
```text
저는 32개월 딸 아이 한명과 현재 임신 8주차 아내를 보살피고 있는 가장입니다.
아빠로써 겪을 심정 고통과 괴로움을 웃음의 방식으로 승화해서 올릴 트윗을 작성해주세요

트윗을 작성 할 때 다음 예문을 참고해주세요

예문1 : 직장과 육아의 갈림길 속에서 겉은 육아를 선택하려는 듯 보이지만 마음은 이미 직장에 가 있다.

예문2 : 어느새 육아 퇴근을 직장 퇴근 보다 더 기다리고 있는 웃픈 현실을 마주하다
```
<br>

### X(구 트위터) API Key 얻기

필요한 5가지 key
- Access Token
- Access Token Secret
- API Key
- API Key Secret
- Bearer Token

<br>
X(구 트위터) 개발자 플렛폼 : https://developer.x.com/en/

- 화면 오른쪽 상단 [Developer Portal] 클릭 -> [Sign Up for Free Account] 클릭

<br>

API KEY 변수명
- API Key : TWITTER_CONSUMER_KEY
- API Key Secret : TWITTER_CONSUMER_SECRET
- Access Token : TWITTER_ACCESS_TOKEN
- Access Token Secret : TWITTER_ACCESS_TOKEN_SECRET
- Bearer Token : TWITTER_BEARER_TOKEN





