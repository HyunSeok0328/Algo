### [UDP 프로토콜](https://youtu.be/3MkI3FBFzX8?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

UDP가 하는일

비연결지향형 (신뢰성이 낮음)

* 사용자 데이터그램 프로토콜은  Universial Datagram Protocol이라고도 일컫기도 한다.
* UDP의 전송 방식은 너무 단순해서 서비스의 신뢰성이 낮고, 데이터그램 도착순서가 바뀌거나, 중복되거나, 심지어는 통보없이 누락시키기도 한다
* UDP는 일반적으로 오류의 검사와 수정이 필요 없는 프로그램에서 수행하는것으로 가정한다

UDP 프로토콜을 사용하는 대표적인 프로그램들

* 도메인을 물으면 IP를 알려주는 DNS서버 !
* UDP로 파일을 공유하는 TFTP 서버 
* 라우팅 정보를 공유하는 RIP(Routing Information Protocol) 프로토콜 최신 라우터를 알게 해줌

### [tftpd로 파일 전송 실습](https://youtu.be/5Woau-EJChw?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

-UDP 같은걸로 파일을 전송할때는 특수한 경우에만 사용 동영상 스트리밍 서비스

운영체제가 설치되지 않는곳에 운영체제의 cd를 전달하거나 할때 (정상적이지 않을때)

NAT(Network Adress Translation) 네트워크 주소 변환 !

사설 IP를 공인 IP로 바꾸는데 사용 따라서 IP 주소 절약 가능 

사용하는 이유 : 보안 (IP를 숨길 수 잇음)



