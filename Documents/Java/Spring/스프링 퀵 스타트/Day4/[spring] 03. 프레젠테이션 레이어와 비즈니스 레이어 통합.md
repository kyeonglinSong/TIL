200229(토)

# [spring] 03. 프레젠테이션 레이어와 비즈니스 레이어 통합



지금까지는 controller의 메서드가 request를 처리할 때 DAO 객체를 직접 이용함

-> 직접 이용하면 안됨! **비즈니스 컴포넌트**를 이용해서 접근해야 함.



### 1. 비즈니스 컴포넌트 사용

 **Controller 메서드에서 DAO를 호출하면 안되는 이유**

- 유지보수 과정에서 DAO를 쉽게 교체하기 위해서

- AOP 적용 때문에

  

#### DAO 클래스 교체하기

Controller 클래스에 Service 객체를 생성함 -> 모든 DAO 삭제 -> DAO를 service 객체로 변경



#### AOP 설정 적용하기

어드바이스가 동작하려면 반드시  service 구현 클래스의 비즈니스 메서드가 실행되어야 한다.





### 2. 비즈니스 컴포넌트로딩

#### 2-layerd 아키텍쳐

일반적인 프레임워크 기반 웹 프로젝트는 **2-layer 아키텍쳐 스타일**로 개발한다.![IMG_FEED4D9A0D54-1](/Users/blossommilktea/Downloads/IMG_FEED4D9A0D54-1.jpeg)





####ContextLoaderListner 등록

ContextLoaderListner : applicationContext.xml 파일을 읽어 비즈니스 컴포넌트를 메모리에 생성하는 역할



- Listener 태그를 이용하여  **web.xml** 파일에 등록한다.
- applicationContext.xml 파일을 읽게 하기 위해서 **web.xml에 context-param 설정을 추가**한다.

![image-20200229122353339](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200229122353339.png)





### 3. 스프링 컨테이너의 관계

![IMG_879F58FB92BA-1](/Users/blossommilktea/Downloads/IMG_879F58FB92BA-1.jpeg)

Servlet Container -> Spring Container(Root) -> Spring Container 순서로 구동된다.

