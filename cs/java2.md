
스프링을 사용한 웹앱의 경우 DAO, DTO, Repository, Entity를 사용하여 데이터를 다루는데
스프링부트의 경우 내장 톰캣을 통해 서블릿을 관리하고 이를 컨트롤러에서 각 어노테이션을 통해 매핑한다.

도메인(엔티티)의 경우 가장 Persistence Layer에 가까운데 이를 이용하기 위해 사용하는 방법들을 알아본다.

## Repository

- MVC 패턴에서 모델에 해당하는 부분으로 POJO로는 접근불가
- Persistence Layer와 1:1 매칭
- Java Persistence API 구현체를 이용하여 자바 객체로 접근할 수 있다.

```null
@Repository 
@RequiredArgsConstructor
public class MemberRepository{

    private final EntityManager em; 

    public void save(Member member) {
        em.persist(member);
    }
```

여기서는 JPA 구현체인 Entity Manger 객체를 사용하여 DB에 접근

## DAO(Data Access Object)

- 원래 DB의 데이터와 프로그래밍 언어는 패러다임의 불일치로 인해 사용할 수 없다
  따라서 별도의 SQL을 작성하고 SQL을 객체의 필드에 하나씩 매핑하거나 순수한 SQL을 작성하여 사용해야 한다.

### Entity

하지만 별도의 Entity Class를 사용하여 그 클래스를 테이블과 1:1 매칭할 수 있다.
이러한 Entity Class를 도메인이라고 하며 가장 DB와 가까운 클래스다.

```null
@Entity
@Getter
public class Member {
    @Id @GeneratedValue
    @Column(name = "member_id")
    private Long id; // PK

    @NotEmpty
    @NotNull
    private String name;

    @Embedded // 내장 타입 임베딩
    private Address address;

    @JsonIgnore
    @OneToMany (mappedBy = "member")
    private List<Order> orders = new ArrayList<>();
}
```

- 엔티티의 각 필드는 DB 테이블과 1:1 매칭되며 따라서 PK를 가진다.
- 엔티티는 순수한 도메인 로직과 비즈니스 로직만 가지고 있어야한다.
  엔티티는 DB의 데이터를 전달해주고 Serivce에서 사용할 비즈니스 로직만을 가져야한다.

```null
@Service
@Transactional(readOnly = true)
@RequiredArgsConstructor
public class MemberService {

    private final MemberRepository memberRepository; // 서비스 계층의 Repository 시용
```

## DTO(Data Transfer Object)

![img](https://media.vlpt.us/images/agugu95/post/189b4d5e-002c-4e7c-a4fb-89f0dd60f435/image.png)
Entity를 통해 DB에서 데이터를 꺼내왔지만 한가지 문제가 있다.
요청을 받고 데이터를 처리하고 반환해주기 위해선 데이터에 접근해야 하는데
여기서 Controller, Presentation Layer의 경우 클라이언트와 직접 맞닿는 부분이고
엔티티는 프레젠테이션 계층과 완전히 분리되어야 한다

이럴 때 DTO를 사용하는데

```null
    @Data
    @AllArgsConstructor
    static class MemberDto {
        private String name;
        private Address address;
    }
```

- Getter/Setter 없음
- Wrapping 된 순수한 데이터 객체
- 엔티티에 직접 접근하지 않기때문에 엔티티가 변경되어도 DTO만 변경하면 된다

## 스프링 프로젝트 구조

![img](https://media.vlpt.us/images/agugu95/post/189b4d5e-002c-4e7c-a4fb-89f0dd60f435/image.png)
결론적으로 스프링 프로젝트는 다음과 같은 구조를 가지게 된다

### Domain(Entity)

```null
@Entity
@Getter @Setter
public class Member {
    @Id @GeneratedValue
    @Column(name = "member_id")
    private Long id;
```

- DB 테이블과 1:1 매칭
- 현재 관련된 객체 없음

### Repository(DAO)

```null
@Repository
@RequiredArgsConstructor
public class MemberRepository{

    private final EntityManager em;
```

- Entity를 통해 데이터를 DB에 저장
- 엔티티는 DB의 데이터와 매칭되는 것
  실제 DB에 데이터를 저장하는 건 Repository 클래스의 Entity Manager를 통해 이루어진다

### Serivce

```null
@Service
@Transactional(readOnly = true)
@RequiredArgsConstructor 
public class MemberService {

    private final MemberRepository memberRepository;
```

- 프레젠테이션(뷰)에서 엔티티에 직접 접근하지않고 비즈니스 로직을 처리할 수 있도록하는 계층
- Repository에 정의된 비즈니스 로직을 처리하거나 엔티티에 접근

### Controller

```null
@RestController // Response + Request
@RequiredArgsConstructor
public class MemberApiController {
    private final MemberService memberService;
    
    @GetMapping("api/v1/members")
    public Result<List<MemberDto>> memberV2() {
```

- 프레젠테이션 계층으로 클라이언트의 요청을 처리
- 엔티티는 서비스에 의해 추상화되어 직접 접근 불가능
- 서비스에 정의된 비즈니스 로직을 호출
- ResponseBody에 데이터를 담아 반환해준다