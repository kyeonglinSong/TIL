200227(목)

# [spring] 07. 트랜잭션 처리

스프링에서는 트랜잭션 처리를 컨테이너가 자동으로 처리하도록 설정할 수 있다. -> **선언적 트랜잭션 처리**

스프링 트랜잭션 설정에는 XML 기반의 AOP가 사용된다. (어노테이션은 사용할 수 없음)

애스팩트 설정도 aop:advisor 엘리먼트만 사용할 수 있다.



#### 1. 트랜잭션 네임스페이스 설정

![image-20200227152020044](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200227152020044.png)

​																	applicationContext.xml



#### 2. 트랜잭션 관리자 등록

모든 트랜잭션 관리자는 PlatformTransactionManager 인터페이스를 구현한 클래스들이다.

commit()과 rollback() 메소드를 가지고 있다.

지금은 **DataSorceTransactionManager**  를 이용하여 트랜잭션 처리를 할 것임.



스프링 설정 파일에 DataSorceTransactionManager 클래스를 bean 등록한다.

![image-20200227152730614](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200227152730614.png)

​																	applicationContext.xml



#### 3. 트랜잭션 어드바이스 설정

![image-20200227152913534](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200227152913534.png)

​																	applicationContext.xml





#### 4. AOP 설정을 통한 트랜잭션 적용

applicationContext.xml 의 전체 설정

![image-20200227153240063](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200227153240063.png)











