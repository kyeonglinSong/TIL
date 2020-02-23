200222(토)

# [Spring] 05. 어노테이션 기반 설정



### 1. 어노테이션 설정 기초

#### context 네임스페이스 추가

bean 엘리먼트에 context 관련 네임스페이스와 스키마 문서 위치를 등록해야 한다.

![image-20200222160654567](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200222160654567.png)



#### 컴포넌트 스캔 설정

```
<context:component-scan base-package="polymorphism"></context:component-scan>
```



이제 applicationContext.xml 파일에 일일이 빈 등록할 필요 없이 `@Context("name")` 어노테이션을 설정하하면 된다!





### 2. 의존성 주입 설정

#### @Autowired

생성자, 메서드 등 모두에게 사용할 수 있다. 해당 변수 타입을 체크한 후, 그 타입의 객체를 변수에 주입한다.



#### @Qualifier

의존성 주입 대상이 되는 객체가 두 개 이상일 때, 의존성 주입될 객체의 아이디나 이름을 지정.



#### @Resource

**@Autowired**는 변수 타입을 기준으로 객체를 검색하여 DI를 처리한다. 반면 **@Resource**는 객체의 이름을 이용하여 의존성을 주입한다.



*테스트 아닌 테스트를 해 보니, xml 설정과 의존성 주입이 둘 다 있을 경우 xml 설정이 우선인 듯 하다.* 



#### 어노테이션과 xml 설정 병행하기

**각각의 장,단점**

- 어노테이션 : xml 설정에 대한 부담 X / 자바 소스를 수정해야 함
- xml : 자바 소스를 수정하지 않아서 유지보수가 편리하다. / xml 설정과 설정 해석에 대한 부담



-> 서로의 장점을 조합하면 훨씬 편리해진다. 

1. 어노테이션 @Autowired 만 사용 + xml에 주입할  bean 하나만 등록
2. 필요시 xml 파일의 bean 클래스 경로를 수정





### 3. 추가 어노테이션

MVC에 대한 어노테이션 설명. 뒤에서 공부할 예정.



#### @Component 를 상속하는 어노테이션

- @Service : 비즈니스 로직 처리, Service 클래스
- @Repository : 데이터베이스 연동 처리, DAO 클래스
- @Controller : 사용자 요청 제어, Controller 클래스



