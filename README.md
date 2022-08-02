## Quick Start  
```
학습 관리 서비스 Hi Class에 접속해보세요!
https://hmys-hiclass.paas-ta.org/
```
## DEMO  
[https://www.youtube.com/watch?v=NjNh38PI3P4](https://www.youtube.com/watch?v=NjNh38PI3P4)
## 시연 알림 사항
- 첫수업의 경우 학생들이 만든 지난수업 복습퀴즈는 없기 때문에 생략 됩니다.
- My Class(수업 관리) 시연시에는 데이터들을 잘 보여주기 위해서<br> 아래의 아이디로 로그인하여 __데이터베이스__ 수업을 확인 할 수 있습니다.

 구분  | ID|PW|
|-------|---------------------|-------|
|&nbsp;학생| sksmsgkstlr@naver.com | 123|
|선생님 | sosick0412@gmail.com  | 123|


# Hi Class,   또 하나의 선생님  
*HiClass(하이클래스) :: 또 하나의 선생님*

언택트 교육의 집중도 및 참여도 저하 문제를 해결하고 유학생&다문화 가정의 수업 이해를 돕는 서비스입니다. 수업 시 학생의 집중도와 참여도 향상을 위한 여러 서비스와 번역, 자막 서비스를 제공하는 **화상 교육 플랫폼**입니다.  
![sysnop](https://user-images.githubusercontent.com/48875061/142240838-8596439e-b334-47e6-97b7-5c26481a42ac.png)  

## 📋 Core Service Logic  

![ourservice](https://user-images.githubusercontent.com/48875061/142241756-15c5fecd-e496-4b1b-bca1-3b34f08052d9.png)
- 실시간 다중 화상 공유 수업
- 선생님이 직접할 필요없이 자동화된 얼굴인식을 통한 출석체크
- 수업 방해 요인 SNS APP 차단
- 학생의 수업 집중도 & 참여도 체크를 위한 자리이탈 감지
- 실시간 수업 번역 및 자막
- 필기 노트 
- 수업 이해도 확인을 위한 마무리 Quiz & 복습 Quiz 
- 수업 태도 확인을 위한 집중도 및 참여도 그래프
- 실시간 채팅 
- 수업 별 공지사항
## ⌨ Service Flow  
![serviceflow](https://user-images.githubusercontent.com/48875061/142242110-7443ec09-e1db-4751-a4e9-ac9becfa606d.png)

## 💡 Service UI(example)  
선생님 홈 화면            |  APP 홈 화면
:-------------------------:|:-------------------------:
![캡처2](https://user-images.githubusercontent.com/48875061/142723204-32f36709-6c01-432b-8183-f267e8b24c7e.PNG) |  ![app](https://user-images.githubusercontent.com/48875061/142244903-5640b9de-6985-4b25-979d-e2b7d282eeb4.png)  

출석체크          |  집중도 통계자료
:-------------------------:|:-------------------------:
 ![culsuk](https://user-images.githubusercontent.com/48875061/142245689-ec5b72e0-017e-4a93-9b41-33caff5edd49.png) |  ![focus](https://user-images.githubusercontent.com/48875061/142245861-62466d72-7087-4c1d-84aa-ba8b2c28cb88.png)


공지사항           |  APP 자리이탈 감지
:-------------------------:|:-------------------------:
 ![gonggee](https://user-images.githubusercontent.com/48875061/142245073-9387dd34-3c1f-46f8-be45-cbcb513e266a.png)| ![seatleave](https://user-images.githubusercontent.com/48875061/142245335-5bc8d0da-c81b-4a64-aa71-d196331c2e5c.png)  

## 💻 Development Stack  

![develop](https://user-images.githubusercontent.com/48875061/142246292-9758d9a1-d975-4efc-9c10-b47dcce5bb5f.png)

## 🔧 Service Architecture  
![창업프로젝트 V2 (4)](https://user-images.githubusercontent.com/48875061/142386854-f6f2a4ca-9173-4f29-97a2-0b7b31a1574b.png)

## 📽️ Video Streaming
![undefined (3)](https://user-images.githubusercontent.com/48875061/142192307-818cfbed-69ea-4977-b628-ab9b01b5f8da.jpg)  
- Peer Connection  
`RTCPeerConnection` 인터페이스는 로컬 컴퓨터와 원격 피어 간의 WebRTC 연결을 담당하며 원격 피어에 연결하기 위한 메서드들을 제공하고, 연결을 유지하고 연결 상태를 모니터링하며 더 이상 연결이 필요하지 않을 경우 연결을 종료합니다.  
- ScreenShare  
`navigator.mediaDevices.getDisplayMedia()`를 통해 화면 콘텐츠를 가져오고
임시 피어를 생성하여 원격 피어 간 연결 유지합니다.  
- Sturn Server  
공개적 주소를 발견하거나 Peer간의 직접 연결의 막는 등의 라우터의 제한을 결정하는 프로토콜입니다. 클라이언트는 인터넷을 통해 클라이언트의 공개 주소와 라우터의 NAT 뒤에 있는 클라이언트가 접근 가능한지에 대한 답변을 위한 요청을 STUN 서버에 보냅니다.
- ICE(Interactive Connectivity Establishment)  
브라우저가 Peer을 통한 연결이 가능하게 해주는 프레임워크 입니다. ICE는 이러한 작업을 수행하기 위해 STUN 서버를 사용합니다.
- SDP(Session Description Protocol)  
해상도나 형식, 코덱, 암호화등의 멀티미디어 컨텐츠의 연결을 설명하기 위한 표준입니다.


## 📽️ VideoStreaming Features  
필기모드            |  PDF 변환
:-------------------------:|:-------------------------:
![pencil](https://user-images.githubusercontent.com/48875061/142193568-bdda8084-8c90-4945-b9c5-a2aacc0fa179.PNG)  |  ![image](https://user-images.githubusercontent.com/48875061/142193909-fe82fcc5-530b-4b47-a4e0-e0ab4b778da6.png)  
수업 중 필기를 할 경우를 대비해 헤더와 본문을 구분 짓고 다양한 기능을 제공하는 Markdown 언어를 이용하여 작성할 수 있습니다. PDF 변환을 통해 자신의 필기를 저장하는 기능을 제공합니다. javascripts의 eidtor를 담당하는 구성 요소 `codemirror`를 통해서 마크 다운형식으로 필기형식을 가능하게 구현했습니다.|nodejs 모듈인 `html-to-pdfmake`을 이용하여 해당 필기 내용을 pdf 형식을 전환하여 저장하는 기능을 구현했습니다.


실시간 음성인식            |  번역
:-------------------------:|:-------------------------:
![unnamed (1)](https://user-images.githubusercontent.com/48875061/142206008-0f420da5-9ea7-4544-a58f-85920ac1c2ed.png)  |  ![unnamed (2)](https://user-images.githubusercontent.com/48875061/142206015-220090c1-e963-4eda-b95e-0511198d713b.png)  
JavaScript 오픈소스 ( Web Speech API )를 사용하여 React의 실시간 시그널링 서버와 통신하는 Section.js에서 각 사용자의 오디오를 인식하여 적용시켜줍니다.|한국어 처리에 특화되어 있는 NaverCloudPlatform API 인 Papago Translation을 사용하여 STT로 만든 자막을 번역합니다. 이후 실시간 수업 번역 기능을 통해 다문화 가정 학생들의 비대면 수업 이해도를 높여줍니다.

### `Redux`  
![Chatting V2](https://user-images.githubusercontent.com/48875061/142204562-7343036e-acde-47b5-b513-e68503263663.jpg)

기존 연결된 IO를 통해 채팅 기능을 제공합니다. 또한 Redux를 통해 메시지 상태 관리를 분리하여 저장, 유지합니다.  
서버로부터 메세지를 전달받게 되면, Dispatch를 통해 스토어에 저장됩니다.  
UI Component에서 state가 필요하다 판단되면, 스토어로부터 저장된 state값을 불러옵니다.  

## 📂 DB 구성도  
![HiClassDB (2) drawio](https://user-images.githubusercontent.com/48875061/142386960-46f25d7f-4f5d-48e3-a7ff-6625350b5e3b.png)

## 🐹 API

---

1. WebRTC서버:: 실시간 영상 전송 서버 (socket)
2. WebRTC — Node Adapting Server

    기본 url :: [https://pedantic-einstein-75bdbe.netlify.app/](https://pedantic-einstein-75bdbe.netlify.app/)

    `IO` / 방 입장 시 socket connection 설정 위한 offer 마다의 토큰 제공

    `IO` / 방 퇴장 시 socket connection 해제

    `IO` / Join room id 중복검사 , 방(UserData) 입장

    `IO`/ offer 요청한 연결, 나를 제외한 전체 사용자에게 연결 요청

    `IO` / getoffer 요청 받은 연결, 나에게 들어온 연결 요청

    `IO` /message 실시간 채팅을 위한 연결

3. ManageServer

    기본 url :: [https://hmys-hiclass.paas-ta.org](https://hmys-hiclass.paas-ta.org)

    `POST` /  → 사용자 아이디 중복 체크 및 비밀번호 재입력 확인 요청

    `POST` / login → 사용자 아이디 및 비밀번호 요청

    `GET` / logout → 로그아웃
    
    기본 url :: [https://hmys-hiclass.paas-ta.org/home](https://hmys-hiclass.paas-ta.org/home)
    
    `GET` / → 로그인 후 첫 페이지 사용자가 선생과 학생에 따라 다른 html 파일을 render

    `POST` / makeclass → 수업을 생성 (선생님만 가능)

    `GET` / makeroom/success → 생성 성공 후 수업 정보 나열 (선생님만 가능)

    `POST` / enterclass/ → 사용자가 선생이면 'enterclass/makequiz'로, 학생이면 'enterclass/student1'로 render
    
    [Teacher]
    
    `POST` / enterclass/makequiz → 오늘 수업할 내용에 대해서 퀴즈 생성

    `POST` / enterclass/teacher → WebRTC 입장
    
    `POST` / classout/teacher → 수업 종료
    
    `POST` / myclass/teacher → 생성한 Class list를 요청
    
    `POST` / myclass/teacher/<int:pk> → 클릭한 Class의 공지 사항을 요청
    
    `POST` / myclass/teacher/<int:pk>/<int:pkk> → 클릭한 공지 사항의 세부 사항을 요청
    
    `POST` / myclass/teacher/<int:pk>/makenotice → 공지 사항 생성
    
    `POST` / myclass/teacher/quiz → 해당 Class의 모든 quiz를 요청
    
    `POST` / myclass/teacher/quiz/<int:pk> → 클릭한 quiz의 세부 사항을 요청
    
    `POST` / myclass/teacher/analytics → 해당 Class의 모든 통계자료를 요청
    
    `POST` / myclass/teacher/analytics/<int:pk> → 클릭한 통계자료의 세부 사항을 요청
    
    [Student]
    
    `POST` / enterclass/student1 → 앱 연동 여부를 요청
    
    `POST` / enterclass/student2 → 얼굴인식을 통해 출석부에 존재 여부 요청
    
    `POST` / enterclass/studentquiz → 다른 학생들이 만든 지난수업 복습퀴즈 정답 여부 
    
    `POST` / enterclass/student3 → WebRTC 입장
    
    `POST` / classout/student → 앱 연동 해제 여부 요청
    
    `POST` / classout/student/makequiz → 오늘 수업에 대한 복습 퀴즈 생성
    
    `POST` / classout/student/teacherquiz → 선생님이 만든 오늘수업 학습확인 퀴즈 정답 여부
    
    `GET` / classout/student/analytics/<int:quiz> → 학습확인 퀴즈의 틀린 횟수를 quiz로 전달하고 
    
    앱에서 전달 받은 앱차단, 자리이탈 점수를 기반으로 집중도 통계자료를 나타냄
    
    `POST` / myclass/student → 입장 했던 Class list를 요청
    
    `POST` / myclass/student/<int:pk> → 클릭한 Class의 공지 사항을 요청
    
    `POST` / myclass/student/<int:pk>/<int:pkk> → 클릭한 공지 사항의 세부 사항을 요청
    
    `POST` / myclass/student/quiz → 해당 Class에서 학습 했던 quiz만 요청
    
    `POST` / myclass/student/quiz/<int:pk> → 클릭한 quiz의 세부 사항을 요청
    
    `POST` / myclass/student/analytics → 해당 Class의 본인의 통계자료만 요청
    
    `POST` / myclass/student/analytics/<int:pk> → 클릭한 통계자료의 세부 사항을 요청
    
3. Android

    기본 url :: [https://hmys-hiclass.paas-ta.org](https://hmys-hiclass.paas-ta.org)

    `POST` / app_login → 로그인 요청

    `POST` / app_signup → 회원가입
    
    `POST` / home/app_enter_room → 방 아이디와 비밀번호를 통한 수업 존재 요청
    
    `POST` / home/app_attendance → 학번(출석번호) 이름을 통한 출석체크
    
    `POST` / home/app_checkimg → 출석체크를 위한 얼굴 일치 여부 요청

    `POST` / home/app_checkin → 앱 인증 완료했다는 정보 전달

    `POST` / home/app_sendcount → 수업 퇴장 후 사용자 sns앱 접근 회수와 자리이탈 횟수 전달

---

### 🙋‍♂️Role

`@ 김유림`  
* PaaS-TA_Android_Client
  - *Android 담당*
  - *로그인/회원가입 구축*
  - *Class 입장 구축*
  - *얼굴인식 출석체크 구축*
  - *특정(sns)앱 접근 차단*
  - *자리이탈 확인 OpenCV 구축*
  - *Retrofit2 통신*  

* PaaS-TA_Manage_Server
  - *퀴즈 생성 및 풀기 구축*
  - *안드로이드 통신*
  
 `@ 김준영`
* PaaS-TA_Realtime-Client
  - *VideoStreaming Layout 구축*
  - *WebSocket token을 활용한 peer connection*
  - *화면 공유 기능 구축*
  - *Chat 기능 구축*
  - *필기 기능 구축*
  - *백엔드 실시간 통신 구축*
  - *Redux를 활용한 상태 관리*

* PaaS-TA_Realtime_Server
  - *WebRtc를 위한 시그널링 서버 구축*
  - *WebSocket token을 활용한 peer connection*

 `@ 김혜원` 
  - *Paas-Ta를 이용한 배포*
* PaaS-TA_Realtime-Client
  - *실시간 음성인식 구축*
* PaaS-TA_Realtime_Server
  - *번역 기능 구축*
* PaaS-TA_Manage_Server
  - *자동출석체크를 위한 얼굴 인식* 

`@ 황한식`
* PaaS-TA_Manage_Server
- *django UI/UX 전체 frontend 개발*
- *django Rest API 설계 및 개발*
- Luxand API 얼굴인식을 통한 자동출석 기능 구축
- *로그인/회원가입 개발*
- *사용자 이미지 변경이 가능한 my page 개발*
- *Class 생성 및 입장 개발*
- *집중도 통계자료 그래프 기능 개발*
- *공지사항 기능 개발*
- *퀴즈&관리 기능 개발*


### License
```
MIT License

Copyright (해몽유식) [2021-11-19] [JunYoung Kim,HyeWon Kim,HanSik Hwang, YouLim Kim]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
