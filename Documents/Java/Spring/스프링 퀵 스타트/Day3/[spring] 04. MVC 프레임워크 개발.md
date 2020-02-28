200228(금)

# [spring] 04. MVC 프레임워크 개발

### 1. MVC 프레임워크 

**03** 에서는 하나의 DispatcherServlet 클래스로 controller의 기능을 모두 구현함 -> 유지보수의 어려움

-> **MVC 프레임워크**를 사용해서  **controller**를 구현하는게 좋음 -> 하지만 어려움ㅠㅠ

-> 따라서, 먼저 **MVC 프레임워크와 동일한 구조의 프레임워크를 직접 구현**하여 적용해볼 것임.



​					(MVC 프레임워크 구조 그림 넣을거임)



#### Container

- DispatcherServlet : 유일한 서블릿 클래스. request를 가장 먼저 처리한다.(front controller)
- HandlerMapping : 클라이언트의 request를 처리할 controller 매핑해줌.
- Controller : 실제 request 처리
- ViewResolver : controller가 리턴한 view 이름으로 실행할 JSP 경로 완성





### 2. MVC 프레임워크 구현

####Controller

- Controller 인터페이스 작성

  모든 컨트롤러를 같은 모양으로 관리하기 위해서 인터페이스를 만든다.

  

- Controller 클래스 구현

  DispatcherServlet 에서 필요한 `_.do` 부분의 소스를 복사해온다.

  

#### HandlerMapping

- HandlerMapping 클래스 작성

  HandlerMapping 클래스는 **모든 controller 객체들을 저장**해놓고, request에 따라 **특정 controller를 검색**하는 기능을 제공한다.

  DispatcherServlet이 사용하는 객체이므로, DispatcherServlet이 생성되고 init() 메서드가 호출될 때 **단 한 번 생성**된다.



####ViewResolver 

- ViewResolver 클래스 작성

  controller가 리턴한 view 이름에 접두사나 접미사를 결합하여 **최종적으로 실행될 view 경로와 파일명을 완성**한다.

  DispatcherServlet이 생성되고 init() 메서드가 호출될 때 **단 한 번 생성**된다.

  

#### DispatcherServlet

- DispatcherServlet 수정

  **front controller**. `init()` 메서드가 정의되어 있다.



#### 최종 프로젝트 구조

![image-20200228154249040](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200228154249040.png)





### 3. EL/JSTL 을 이용한 JSP 화면 처리

JSP에서 자바 코드를 모두 제거하고 싶을 때 이용한다.

- pom.xml에 jstl을 추가한다.

  