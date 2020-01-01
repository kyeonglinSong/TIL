200101(수)

#스프링 IoC 컨테이너



###IoC 컨테이너

역할 : 빈을 만들고 빈들사이의 의존성을 엮어주며 컨테이너가 가지고있는 빈들을 제공해준다.



- beanfactory 나 applicationceontext사용

- applicationcontext는 beanfactory상속. 고로 더 많은 일을 해줌



* -controller, -Repository 여기있는애들이 주로 빈
  * 빈인지 아닌지 어떻게아는가? 
    * 인텔리제이의 왼쪽 녹색 콩 표시 : 빈
    * owner은 빈 아님ㅋㅋㅋ / ownerController는 빈
    * 빈 등록방법 : 어노테이션(직접 빈 등록), 특정 인터페이스 상속
  * 오너컨트롤러는 오너리퍼지토리타입 사용. 이 객체는 애플리케이션 컨텍스트(스프링 아이오씨 컨테이너)가 타입의 빈을 찾아서 넣어줌
  * 의존성 주입은 빈끼리만 가능하다. 즉 스프링 ioc 컨테이너 안의 객체들끼리만 의존성 주입이 가능함. 밖에있는 객체는 안됨.
  * ~~테스트에서 빈을 사용해볼 수 있음
  * applicationContext안에 모든 빈들이 들어있음. -> 이걸 사용해서 이 안의 빈들을 조회가능



- 빈과 일반 객체의 차이
  - applicationContext가 담고 있는 객체는 빈
    - bean으로 만드는 객체만 의존성 주입이 됨,
  - 직접 new로 해서 만드는 객체는 일반 객체



어떻게 특정한 인스턴스를 빈으로 만드는가?

- 컴포넌트 스캔 : @Component 애노테이션

  - Ioc 컨트롤러를 만들고 등록할 때 사용하는 인터페이스들 : 라이프사이클 콜백
  - ComponentScan : 애노테이션이 ioc 컨테이너가 만들어질때 컴포넌트를 찾으라고 알려줌

  -> 컴포넌트 붙어있는데부터 모든 하위 패키지, 클래스를 다 훑으면서 @controller, @component 애노테이션 등이 있는 애들을 빈으로 만들어줌

  

- 직접 빈 등록 

  - 자바설정파일 : @Configuration이라는 애노테이션 붙음

  - 클래스 안의 @bean 애노테이션 아래의 애들 빈으로 등록됨

    

- 리파지토리 : JPA에 의해 빈으로 등록됨. 특정 인터페이스를 상속받음. 인터페이스의 구현체를 만들어서 빈으로 만들어줌.



- 빈 꺼내쓰는법 
  - @Autowired 애노테이션 사용  -> 이 방법을 더 많이 사용
  - applicationContext에서 직접 꺼내서 사용(잘 안씀)



* css가 깨질 경우 -> 메이븐으로 패키지 빌드 후 다시 실행





### Dependency Injection

- Autowired 
  - 생성자로 주입받기 : 권장하는 방법
  - 필드 인젝션 : @autowired 스프링 4.3부터 어떤 클래스의 생성자가 하나고 ~~면 자동으로 빈 주입 -> @autowired 애노테이션 생략 가능
  - setter 인젝션 : @Setter 애노테이션
  - 의존성 오류 : No qualifying bean ~~



순환참조(circular dependency) 가 발생하는 경우 생성자 인젝션 못함ㅠㅠ 필드인젝션이나 세터인젝션 사용해야함.



과제

- Ownercontroller에 PetRepository 주입하기