Redis = Remote Dictionary server의 줄인말

외부        haspmap key-value 방식 

외부에 있는 dictionary 자료구조를 사용하는 서버

메모리상에 데이터를 저장하는 서버

다양한 자료구조를 제공함

 cache : 나중의 요청에 대한 결과를 미리 저장했다가 빠르게 사용하는것



![image-20220702232711737](C:\Users\lee\AppData\Roaming\Typora\typora-user-images\image-20220702232711737.png)

메모리 계층구조



* Database보다 더 빠른 Memory에 더 자주 접근하고 덜 자주 바뀌는 데이터를 저장하자

* in-memory Database(cahce)

  이래서 나온게 REDIS

Race Condition이란 여러개의 쓰레드가 경합하면서 context switiching이 발생하고 

이러한 context switching으로 인해 원치않는 결과가 발생함

따라서 redis는 기본적으로 싱글 쓰레드

주의해야될점 : 싱글쓰레드 서버이므로 시간복잡도를 고려해야함

메모리 파편화 : 메모리가 실제로 사용하는것보다 커보임

가상메모리 swap : 

 가상 메모리등의 이해가 필요함