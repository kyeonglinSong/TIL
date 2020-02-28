200228(금)

#[spring] 01-02. 어노테이션 기반 MVC 개발

Xml 설정을 줄이고 싶다 -> 어노테이션을 최대한 활용하자!



#### 1. 어노테이션 관련 설정

Presentation-layer.xml 수정

- Bean 루트 엘리먼트에 context 네임스페이스 추가 (**xmlns:context**)
- controller, handlermapping, viewResolver 클래스에 대한 bean 등록을 **Context:component-scan** 엘리먼트로 대체

![](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200229004558223.png)

​																			 ~~깨끗해졌다..!~~



#### 2. 어노테이션 사용하기

어노테이션을 사용하면 컨트롤러 클래스들을 일일이 bean 등록할 필요가 없다!

xml 파일의 **Context:component-scan** 덕분에 컨테이너가 컨트롤러 객체를 자동으로 생성하기 때문.



**@Controller**

DispatcherServlet 이 인식하는 controller 객체로 만들어준다.

Controller의 리턴타입에는 ModelAndView와 String이 있는데, 대부분 리턴타입을 **String으로 통일**한다.



**@RequestMapping**

@RequestMapping(value="요청") : 해당 메서드를 value에 해당하는 요청에 매핑하겠다. value는 생략 가능.





#### 3. 클라이언트 요청 처리

- controller는 사용자의 request 정보를 추출하여 VO 에 저장

  - 원래는 getParameter()를 통해 입력 정보 추출 -> vo에 저장

  - **command 객체**를 이용하는 방식

    값 매핑할 VO를 매개변수로 선언 -> command 객체에 사용자 request 정보 세팅 -> VO에 넘겨줌

    코드가 훨씬 간단해진다!

    

  - (예시 / insertBoardConteroller.java)

  ![image-20200229011517709](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200229011517709.png)

  - DB연동 자동 처리를 위해 DAO도 매개변수로 선언

  -  vo에 넘겨준 후, 글 목록 출력을 위해 ".do" 를 리턴한다.

  

- 후에 비즈니스 컴포넌트의 메서드는 VO 객체를 인자로 전달받는다.





#### 4. 컨트롤러 통합하기

간결해진 Board 관련 컨트롤러들을 모두 **BoardController** 클래스에 통합해준다.

