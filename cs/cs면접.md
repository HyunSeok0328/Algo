전위 중위 후위

트리와 그래프의 차이 싸이클의 유무

포트번호의 의미 누구와 통신할지 지정해주는것

시간복잡도(빅오 오메가 세타 로테이션)의 의미 설명

프로세스 쓰레드의 개념과 차이점

동기화에 관한것은 cs단골(운영체제 볼 것)

쓰레드 : cpu가 실행하는 최소 실행단위

빅오 빅오메가 빅세타

\1. O(1) : 스택에서 Push, Pop

\2. O(log n) : 이진트리

\3. O(n) : for 문

\4. O(n log n) : 퀵 정렬(quick sort), 병합정렬(merge sort), 힙 정렬(heap Sort)

\5. O(![img](https://t1.daumcdn.net/cfile/tistory/9986834A5C7EBD3007)): 이중 for 문, 삽입정렬(insertion sort), 거품정렬(bubble sort), 선택정렬(selection sort)

\6. O(![img](https://t1.daumcdn.net/cfile/tistory/99D5714E5C7EBD2506)) : 피보나치 수열

루트의 위치를 생각하면서 암기하자

전위 루트가 맨앞

중위 루트가 중간

후위 루트가 마지막

**전위 순회(preorder traverse) : 뿌리(root)를 먼저 방문**

**⊙ 중위 순회(inorder traverse) : 왼쪽 하위 트리를 방문 후 뿌리(root)를 방문**

**⊙ 후위 순회(postorder traverse) : 하위 트리 모두 방문 후 뿌리(root)를 방문**

**⊙ 층별 순회(level order traverse) : 위 쪽 node들 부터 아래방향으로 차례로 방문**

 ![img](https://mblogthumb-phinf.pstatic.net/20120331_173/rlakk11_1333202999001hceVs_JPEG/4.jpg?type=w2)

전위 순회 : 0->1->3->7->8->4->9->10->2->5->11->6

중위 순회 : 7->3->8->1->9->4->10->0->11->5->2->6

후위 순회 : 7->8->3->9->10->4->1->11->5->6->2->0

층별 순회 : 0->1->2->3->4->5->6->7->8->9->10->11
