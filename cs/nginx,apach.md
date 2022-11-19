아파치는 서버는 커넥션을 구축할떄마다 프로세스를 형성하게 되어서 이러면 메모리부족현상이 일어나고 (요청이 없으면 프로세스가 방치됨)

프로그램이 무거워지고 cpu가 과부함

컨텍스트 스위칭이 많아짐 !!

동시커넥션을 감당하기에 아파치서버가 적합하지않음

아파치서버가 가진 구조적 한계를 극복하기 위해 만들어진게 nginx

nginx가 동시커넥션을 유지할 수 있는이유

마스터 프로세스 -> 워커프로세스(실제로 일하는 녀석 listen소켓을 배정받음) 

시간이 오래걸리는 작업은 따로 쓰레드풀을 만들어놓음

보통 워커프로세스는 코어갯수만큼 만들어서 컨텍스트 스위칭 사용을 줄임

엔진엑스는 로드밸러서의 역할도 담당할 수 있음

로드밸런서는 요청을 여러 서버로 분산하는 작업을 수행함

스마트폰 때문에 nginx에 수요가 늘어남

웹에 담기는 콘텐츠가 다양해지고 용량이 커지면서 여러 tcp 커넥션을 동시에 만들기 시작

mpm 멀티프로세스모듈의 약자

동시커넥션관련지표에서 엔진엑스가 아파치서버보다 훨씬 앞섬

아파치는 다양한 os에서 안정적이라는 장점이 있음 지금까지 오랜기간 업데이트해왔기때문에

모듈을 추가해서 확장하기 쉽다는 장점이 있음 현재 잘 돌아가고 있고 모듈의 추가로 극복할 수 있음

그리고 아파치서버가 엔진엑스보다 더 모듈의 종류가 많음

아파치는 윈도우에서 안정적이지 않음 아파치보다

아파치는 안정성 , 확정성 이중요

엔진엑스는 동시커넥션이 중요

엔진엑스는 가볍고 로드밸런서의 역할도 가능해서 웹서버가속기 역할을 함

nginx는 ssl 터미네이션을 수행할 수 있음

ssl터미네이션이란 클라이언트와는 https 통신 서버와는 http 통신을 하는것을 말함

cors 처리도 함