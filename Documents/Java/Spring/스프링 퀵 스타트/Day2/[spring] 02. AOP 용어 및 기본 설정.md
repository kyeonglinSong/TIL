200223(일)

#[spring] 02. AOP 용어 및 기본 설정



### 1. AOP 용어 정리

- **조인포인트**(Joinpoint)

  클라이언트가 호출하는 모든 비즈니스 메서드. (ServiceImpl 클래스의 모든 메서드)

  조인포인트 중 포인트컷이 선택되기 때문에 포인트컷 대상, 포인트컷 후보라고도 한다.

  

- **포인트컷(Pointcut)**

  필터링된 조인포인트.

  

  ![image-20200223152549067](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200223152549067.png)

  포인트컷은 aop:pointcut 엘리먼트로 선언한다.

  

  ![IMG_BE952A50FBB3-1](/Users/blossommilktea/Downloads/IMG_BE952A50FBB3-1.jpeg)

  ​												01에선 이해하지 못했던 포인트컷 표현식 구성과 의미

  

  이제 로그는 get으로 시작하는 메소드에만 반응한다.



- **어드바이스(Advice)**

  횡단 관심에 해당하는 공통 기능의 코드. 독립된 클래스의 메서드로 작성된다.

  어드바이스의 메서드가 언제 동작할지는 스프링 설정파일을 통해 지정할 수 있다.

  

  어드바이스의 동작 시점 

  - befor , after, after-returning, after-throwing, around

  ![image-20200223153544718](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200223153544718.png)

  파란색 부분을 변경하면 동작 시점이 바뀐다.



- **위빙(Weaving)**

  포인트컷으로 지정한 핵심 관심 메서드가 호출될 때 어드바이스에 해당하는 횡단 괌심 메서드가 삽입되는 과정.

  위빙을 통해 핵심 메서드를 건들지 않고 횡단 관심을 추가/변경할 수 있다.

  스프링에서는 **런타임 위빙** 방식만 지원한다.



- **애스팩트(Aspect) or 어드바이저(Advisor)**

  AOP의 핵심! 포인트컷과 어드바이스의 결합

  어떤 포인트컷에 대해 어떤 어드바이스를 실행할지 결정한다.

  

  보통은 aop:aspect를 사용하지만, <u>트랜잭션 설정에서는 aop:advisor를 사용</u>한다.

  

  

  #### 총 정리

  ![IMG_F2C728CAA68B-1](/Users/blossommilktea/Downloads/IMG_F2C728CAA68B-1.jpeg)



 

### 2. AOP 엘리먼트



![image-20200223154833419](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200223154833419.png)

​														(applicationContext.xml의 aop 엘리먼트 부분)



- **aop:config 엘리먼트**

  루트 엘리먼트. 하위에 **aop:pointcut**과 **aop:aspect** 엘리먼트가 위치할 수 있다.



- **aop:pointcut 엘리먼트** 

  포인트컷 지정을 위해 사용된다. 

  

- **aop:asepct엘리먼트**

  핵심 관심에 해당하는 포인트컷 메서드와 횡단 관심에 해당하는 어드바이스 메서드를 결합하기 위해 사용한다.

  <u>얘에 따라 위빙 결과가 달라지므로 제일 중요한 설정이다.</u>

  

- **aop:advisor 엘리먼트**

  트랜잭션에서 사용하는 엘리먼트. 메서드 이름을 확인하지 못할 때 사용한다.





### 3. 포인트컷 표현식

![IMG_BE952A50FBB3-1](/Users/blossommilktea/Downloads/IMG_BE952A50FBB3-1.jpeg)

아까도 나왔던 얘. 설정할때마다 찾아보자..