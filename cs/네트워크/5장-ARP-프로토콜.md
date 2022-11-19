### [ARP 프로토콜](https://youtu.be/LDsp-Xb168E?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

- 같은 네트워크 대역에서 통신을 하기위해 필요한 MAC주소를 IP주소를 이용해서 알아오는 프로토콜
- 데이터를 보내기 위해서는 IP주소와 MAC주소가 모두 필요한데 ARP프로토콜이 있으면 MAC주소를 몰라도 통신이 가능
- 8bit = 1byte

ARP 프로토콜 

- source Hardward Addres 출발지 MAC주소
- Source Protocol Address 출발지 IPv4 주소
- Destination Hardware Address 목적지의 MAC주소
- Destionation Protocol Address 목적지의 IPv4주소
- 대부분은 출발지가 먼저옴 
- 이더넷 프로토콜만 목적지가 먼저옴
- HardWare Type (0 0 0 1 이더넷 프로토콜)
- Protocol Type (프로토콜 어드레스 타입) ex) IPv4(0800) or IPv6
- OPcode(Operation Code) 2개 밖에 없음 1,2 지금 MAC주소를 요청하고 있는지 응답하고 있는지 물어볼 때는 1 응답할때는 2 

### ARP 프로토콜의 통신 과정

- ARP요청 프로토콜을 보냄 
- 목적지 맥주소는 모르기 때문에 00000000으로 비어둠
- Ethnet 프로토콜은 목적지 MAC주소를 모르기 때문에 FFFFFFFFF로 꽉채움 BroadCast가 됨 !!!(모두에게 보냄)
- 스위치 (대표적인 2계층 장비) 2계층까지만 디캡슐레이션 함 ->
- 본인의 IP주소와 목적지주소가 일치하지않으면 버림
- 일치하면 응답프로토콜을 만들어서 다시 보내줌(출발지MAC주소에 자기 MAC주소를 적어서 보내줌)

### ARP 테이블

- 나와 통신했던 컴퓨터 맥주소와 IP주소를 테이블로 정리

### [ARP 프로토콜 실습](https://youtu.be/-M_S50Ga384?list=PL0d8NnikouEWcF1jJueLdjRIC4HsUlULi)

-