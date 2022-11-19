### [TCP 프로토콜](https://youtu.be/cOK_f9_k_O0?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

TCP가 하는일

- 전송 제어 프로토콜은 인터넷에 연결된 컴퓨터에서 실행되는 프로그램 간에 통신을 안정적으로 순서대로 에러없이 교환할 수 있게 한다.
- TCP의 안정성을 필요로 하지 않는 애플리케이션의 경우 일반적으로 TCP대신 UDP를 사용한다
- TCP는 UDP보다 안전하지만 느리다 
- TCP와 UDP의 차이가 체감이 될정도로 속도 차이가 나지않는다



### TCP 플래그

- Urgent : 긴급 비트 (내가 보내는 비트가 우선순위가 높은게 포함되어있다.)
- Acknowledgement (TCP에서 중요하고 자주 사용 **승인비트** 물어보는거에 응답해주는 비트)
- Push(밀어넣기 비트 계속해서 데이터를 밀어넣겟다) 많이 사용안함
- Reset(초기화 비트 상대방이랑 연결되어있는 상태에서 추가적으로 무언갈 할려고하는데 문제가 발생해서 다시 연결하자)
- **Syn**(동기화비트) 상대방이랑 연결시작할떄 무조건 사용하는 플래그로 이 비트가 보내지고 난 후 계속 동기화 하는것 계속 연락하는것 가장 중요한
- Fin 종료비트 연결을 끊을 때 사용

### [TCP 3Way Handshake](https://youtu.be/Ah4-MWISel8?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

- TCP를 이용한 통신과정 

  연결수립과정

  * TCP를 이용한 데이터 통신을 할 때 프로세스와 프로세스를 연결하기 위해 가장 먼저 수행되는 과정
  * 1.클라이언트가 서버에게 요청 패킷을 보내고
  * 2.서버가 클라이언트의 요청을 받아들이는 패킷을 보내고
  * 3.클라이언트는 이를 최종적으로 수락하는 패킷을 보낸다.
  * 위의 3개의 과정을 3Way HandShake라고 부른다.

  

### [TCP를 이용한 데이터 전송 과정](https://youtu.be/0vBR666GZ5o?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

- TCP를 이용한 데이터 통신을 할 때 단순히 TCP 패킷만을 캡슈로하해서 통신하는 것이 아닌 페이로드를 포함한 패킷을 주고 받을 때의 일정한 규칙
- 1. 보낸 쪽에서 또 보낼 때는 SEQ번호와 ACK번호가 그대로이다
  2. 받는쪽에서 SEQ번호는 받은 ACK번호가 된다
  3. 받는쪽에서 ACK번호는 받은 SEQ번호 + 데이터의 크기

### [TCP의 연결 상태 변화](https://youtu.be/yY0uQf0BTH8?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

- 

### [TCP 프로토콜 분석 실습](https://youtu.be/WseqBDo-j3Y?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

-