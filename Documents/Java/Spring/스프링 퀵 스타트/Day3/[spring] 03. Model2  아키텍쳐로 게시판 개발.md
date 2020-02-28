200228(금)

# [spring] 03. Model2  아키텍쳐로 게시판 개발

### 1. Model 2 아키텍쳐 구조

모델1은 화면 디자인과 자바 로직이 통합되어 있어 유지보수가 어렵다. -> model2 **MVC** 아키텍쳐 등장!

**MVC 아키텍쳐** 

- Controller : 서블릿 클래스를 중심으로 구현. 기존 JSP가 담당했던 controller 로직을 별도의 서블릿으로 옮겨감.
- JSP : view와 관련한 디자인 영역만 남게 됨.



**MVC 프레임워크**를 사용하면 더 효율적이고 안정적이다. 그러나 어렵기 때문에 일단은 controller의 기능 이해부터 한다.

![IMG_0989E4DB6DD9-1](/Users/blossommilktea/Downloads/IMG_0989E4DB6DD9-1.jpeg)

​																				MVC (Model 2) 아키텍처





### 2. Controller 구현하기

- Java Servlet 이란? - 자바를 사용하여 웹페이지를 동적으로 생성하는 서버측 프로그램. 자바 클래스의 일종.

  

#### (1) 서블릿 생성 및 등록

​	src/main/java -> 우클릭 후 create new servlet -> 설정 후 등록 ->Web/**web.xml** 에서 서블릿 매핑

![image-20200228141427105](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200228141427105.png)

​																					web.xml

- url-patern의 `*.do`는 do로 시작하는 모든 요청을 이 서블릿 클래스가 처리한다는 의미이다.

#### (2) controller 서블릿 구현

- doGet, doPost 메서드에서는 각각 GET, POST 요청을 받아서 process 메서드로 넘긴다.

- process 메서드에서는 각 패스에 맞게 분기 처리를 한다.



이제 기존 JSP 파일에서 처리 로직을 추출하여 서블릿 클래스에 추가하면 된다!