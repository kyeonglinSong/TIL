200222(토)

# [Spring] 04. 의존성 주입



### 1. 의존성 관리

#### 스프링의 의존성 관리 방법

스프링의 가장 중요한 특징은 객체의 생성과 의존관계를 컨테이너가 자동으로 관리한다는 점이다. (**IoC**)

스프링은 IoC를 두 가지 형태로 지원한다.



- Dependency Lookup
- Dependency Injection



3장까지 사용했던 방식이 Dependency Lookup인데 (객체를 id나 name으로 검색해서 요청하는 방식), 사실 사용하지 않는 방법이다. 대부분은 Dependency Injection을 사용한다.



**Depedency Injection**은 객체 사이의 의존관계를 설정파일을 바탕으로 컨테이너가 자동으로 처리해준다. 따라서 설정 파일만 수정하면 된다.

Dependency Injection은 다시 **Setter Injection**과 **Construction Injection**으로 나뉜다.



![IMG_7F0695CBB565-1](/Users/blossommilktea/Downloads/IMG_7F0695CBB565-1.jpeg)



#### 의존성 관계

객체와 객체의 결합 관계. 하나의 객체에서 다른 객체의 변수나 메소드를 이용하는 것.



**원래대로 의존 관계를 설정할 경우의 문제점**

1. 객체가 쓸데없이 여러 번 생성된다.
2. 변경이 생기면 메서드를 모두 수정해야 함.



-> 스프링은 이를 해결하기 위해 **의존성 주입(Dependency Injection)**을 이용한다.





### 2. 생성자 인젝션 이용하기

스프링 컨테이너는 객체 생성시 디폴트 생성자를 호출한다.

디폴트 생성자 이외에 다른 생성자를 호출하도록 할 수 있는데, 이걸 이용하여 constructor injection을 처리한다.

생성자 인젝션은 <u>생성자의 매개변수로 의존관계에 있는 객체의 주소 정보를 전달</u>한다.



![image-20200222145721493](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200222145721493.png)

​																		applicationConext.xml

constructor-arg에 다른 bean을 적어놓았다.



![image-20200222150252595](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200222150252595.png)



실행 결과. 원래는 빈에 등록된 순서로 객체 생성이되지만, 여기서는 매개변수인 개체가 먼저 생성된다.





#### 다중 변수 매핑

생성자 인젝션에서 초기화해야 할 변수가 여러개이면 그냥 여러개 추가하면 됨!



**Constructor-arg 의 속성**

- ref : 객체를 생성자 인자로 전달할 때 사용.

- value  : 생성자 매개변수로 전달할 값을 지정할 수 있다.

- index : 생성자가 여럿일 때를 위해 지원되는 기능. 어떤 값이 몇 번째 매개변수로 매핑되는지 알 수 있다.





### 3. Setter 인젝션 이용하기

Setter 메서드를 호출하여 의존성 주입을 처리하는 방법.

위의 생성자 인젝션과 세터인젝션 어떤 방법을 사용하든 상관은 없음, 하지만 코딩 컨벤션에 따라서 주로 세터인젝션을 사용한다. 하지만 setter메서드가 제공되지 않는 클래스는 생성자 인젝션을 사용한다.



1. Setter 메소드 생성

2. applicationContext.xml 수정

   ![image-20200222153459472](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200222153459472.png)

   ​																applicationContext.xml

   세터 인젝션에서는 <property>  엘리먼트를 사용한다.





#### p 네임스페이스 사용하기

세터 인젝션에서 p 네임스페이스를 이용하기



1. 먼저 applicationContext.xml 에 `xmlns:p="http://www.springframework.org/schema/p"` 를 추가해준다.

![image-20200222154129057](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200222154129057.png)



2. 기존 <u>property 엘리먼트 대신</u> bean 엘리먼트에 p 네임스페이스를 추가해준다.

![image-20200222154331323](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200222154331323.png)





### 4. Collection 객체 설정

배열이나 리스트같은 컬렉션 객체를 이용하여 데이터 집합을 사용하는 경우가 있다. 이때 컬렉션 객체를 의존성 주입하면 된다. 

스프링에서는 커렉션 매핑과 관련된 엘리먼트를 지원한다.



<List> <Set> <Map> <props> 등등..



하지만 거의 <List> 만 사용함.