### [IPv4 프로토콜](https://youtu.be/_i8O_o2ozlE?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

IPv4가 하는일

- 네트워크 상에서 데이터를 교환하기 위한 프로토콜
- 데이터가 정확하게 전달될 것을 보장하지 않는다 (멀리있는 곳과의 전달의 역할)
- 중복된 패킷을 전달하거나 패킷의 순서를 잘못 전달할 가능성도 있다.
- 악의적으로 이용되면 DoS 공격이 됨
- 데이터의 정확하고 순차적인 전달은 그보다 상위 프로토콜인 TCP에서 보장한다!

IPv4 프로토콜의 구조

* 다른 네트워크의 특정 대상을 찾는 IPv4 프로토콜

### [ICMP 프로토콜](https://youtu.be/JaBCIUsFE74?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

- 상대방과 통신이 되나 안되나 확인하기 위함 !
- 네트워크 컴퓨터 위에서 돌아가는 운영체제에서 오류 메시지들 전송 받는데 주로 쓰인다
- 프로토콜 구조의 Type과 Code를 통해 오류 메시지를 전송 받는다

Type Code

* 0번 Echo Reply 기본(응답)
* 8번 Echo 기본(요청)
* 3번 Destination Unreachable 목적지에 도달 불가(통신안될때) 목적지까지 가질 못한거 (경로설정 잘못한거)
* 11번 Time Exceded 요청시간이 만료(통신 안될 때) 상대방이 방화벽 있을경우가 대부분
* 5번 보안상

### [IPv4, ICMP프로토콜 실습](https://youtu.be/8ZwTvTuZlVw?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

- 

### [라우팅 테이블](https://youtu.be/CjnKNIyREHA?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

스위치 : 정보를 동시에 주고 받을 수 있어 허브보다 빨리정보를 주고 받음

- 최적의 경로를 지도처럼 저장하고 있는거 
- netstat -r로 저장 되어있음
- 경로가 저장되어있는 것만 찾아갈수 있음 없으면 찾아갈 수 없음
- 내 컴퓨터에서 보낸 ㅐ킷이 다른 네트워크의 컴퓨터까지 어떻게 이동하는가 ?~



### [라우팅 테이블 확인 실습](https://youtu.be/tVntagSJctc?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

- 

### [IPv4 조각화 이론](https://youtu.be/_AONcID7Sc8?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

- 큰 IP 패킷들이 적은 MTU(Maximum Transmission Unit)를 갖는 링크를 통하여 전송되려면 여러 개의 작은 패킷으로 쪼개어/조각화 되어 전송돼야 한다.
- 즉 목적지까지 패킷을 전달하는 과정에 통과하는 각 라우터마다 전송에 적합한 프로엠으로 변환이 필요하다.
- 일단 조각화되면, 최종 목적지에 도달할 때까지 재조립되지 않는것이 일반적이다.
- IPv4에서는 발신지 뿐만 아니라 중간 라우터에서도 IP 조각화가 가능하다
- IPv6에서는 IP단편화가 발신지에서만 가능하다
- 재조립은 항상 최종수신지에만 가능하다
- MF(More Fragment 내뒤에 데이터가 있는지 없는지 알려줌 있으면 1 없으면 0)

### [IPv4 조각화 실습](https://youtu.be/QKEL9aBgHtg?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

-