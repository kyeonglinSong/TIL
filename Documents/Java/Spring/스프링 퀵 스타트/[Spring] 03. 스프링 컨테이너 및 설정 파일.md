200222(토)

# [Spring] 03. 스프링 컨테이너 및 설정 파일



### 1. 스프링 컨테이너 시작하기

대부분의 IoC컨테이너는 각 컨테이너에서 관리할 객체들을 위한 설정 파일이 있다.

(ex)

- servlet -> web.xml

- EJB -> ejb-jar.xml



#### 인텔리제이에서 스프링 환경설정 파일 생성 

1.  resources -> new -> XML Configuration File -> Spring Config 을 클릭하면 자동으로 <bean> 엘리먼트 설정들이 추가된다.

2. <bean> 엘리먼트에 클래스를 추가한다.

![image-20200222133903078](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200222133903078.png)



####스프링 컨테이너 구동 및 테스트

객체를 테스트하는 클라이언트를 만들기

![image-20200222134219509](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200222134219509.png)

위에서 만든 xml 파일을 로딩한다. 



![IMG_F70C492ED0F5-1](/Users/blossommilktea/Downloads/IMG_F70C492ED0F5-1.jpeg)





#### 스프링 컨테이너의 종류

스프링에서는 **BeanFactory**와 이를 상속하는 **ApplicationContext** 두 가지 유형의 컨테이너를 제공한다.

- **BeanFactory** : 스프링 설정 파일에 등록된 <bean> 객체를 생성, 관리. 

  클라이언트의 요청에 의해서만 bean 객체를 생성한다. (**lazy loading**)

- **ApplicationContext** : BeanFactory의 기능 + 트랜잭션 관리 등의 다양한 기능

  컨테이너가 구동되는 시점에 즉시 객체를 생선한다. (**pre-loading**)

  웹 애플리케이션 개발도 지원 

  - GenericXmlApplicationContext : XML 설정파일을 로딩하여 구동하는 컨테이너
  - XmlWebApplicationContext : 웹 기반 스프링 애플리케이션 개발에 사용하는 컨테이너

  

대부분의 스프링 프로젝트는 **ApplicationContext** 유형의 컨테이너를 사용한다.







### 2. 스프링 XML 설정

스프링 컨테이너는 xml파일을 참조하여 빈의 생명주기 관리, 서비스 제공

그래서 설정파일 작성 엄청중요함

bean이 루트 엘리먼트, bean description alias import 가 자식 엘리먼트로 사용될수있음. 실제론 bean이랑 import 정도 많이 씀



#### import

설정 파일들을 하나로 통합할 때 사용



#### bean

스프링 설정 파일에 클래스를 등록할때 사용

id는 생략가능, class는 필수. 정확한 경로 입력해야함

그치만 클라이언트가 객체를 요청(lookup) 하려면 id 속성이 꼭 필요하다. 없으면 에러뜬다. 컨테이너가 각 객체를 식별해야하기 때문이다. 

![image-20200222140920285](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200222140920285.png)

​																	~~(id 값이 없어서 생기는 에러)~~

id 말고 name으로 써도 된다. name은 특수기호를 포함할 수 있다.





#### bean 엘리먼트의 속성

- init-method

컨테이너가 객체를 생성할때 디포ㄹ트 생성자를 호출한다. 나중에 멤버변수 초기화 작업이 필요할 때 init() 메소드가 필요하다. 이를 init-method 속성이 있음!

![image-20200222141433985](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200222141433985.png)

​																applicationContext.xml 



그 후 클래스에다 initMethod 를 작성해주면 된다.



- destroy-method

컨테이너가 객체를 삭제하기 직전에 호출될 메소드 지정



- lazy-init 

applicationContext는 즉시 로딩 방식을 사용한다. 하지만 자주 사용하지도 않는데 메모리를 차지하면 시스템에 부담을 줄 수 있으니, 그런 애들은 lazy-init으로 등록해버리자.

` lazy-init="true"`



- Scope

개발을 하다보면 많은 객체가 생기는데, 그 중에는 하나만 생성되도 상관 없는 객체들도 있다. 

가장 좋은 방법은 객체가 한 번만 생성되도록 자동으로 singleton 객체로 생성해주면 된다. 스프링에서는 컨테이너가 이 기능을 제공한다. 

scope를 사용하여 bean의 범위를 지정할 수 있는데, 기본값은 싱글톤이다. 

매번 새 객체를 만들고 싶으면 scope 설정을 `scope="prototype"` 으로 지정해주면 된다.











