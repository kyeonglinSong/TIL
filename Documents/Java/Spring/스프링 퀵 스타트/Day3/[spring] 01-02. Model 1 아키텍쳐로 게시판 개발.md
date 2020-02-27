200227(목)

#[spring] 01-02. Model 1 아키텍쳐로 게시판 개발



### 1. Model 1 아키텍쳐 구조

![IMG_CC381C6A8E0C-1](/Users/blossommilktea/Downloads/IMG_CC381C6A8E0C-1.jpeg)



- **JavaBeans **

  model 기능, 데이터베이스 연동에 사용되는 자바 객체들. VO, DAO 클래스

- **JSP**

  controller와 view 기능을 모두 처리한다.

  - controller : JSP에 작성될 사용자의 요청 처리와 관련된 자바 코드  
  - view : HTML, CSS 마크업을 통해 데이터를 사용자가 원하는 화면으로 제공

  

Model 1 구조는 JPS 파일에서 controller와 view를 모두 처리함 -> 역할 구분이 명확하지 않다 -> 유지보수에 어려움

따라서 간단한 프로젝트를 수행할 때는 사용하기 좋으나, 엔터프라이즈 급의 시스템에는 부적절함.

(Model 2는 MVC 아키텍쳐. 다음 장에 자세히 나옴.)





###2.  Model 1 구조로 개발

#### forward와  redirect의 차이

- forward :  jsp 요청 -> 다른 jsp로 forwarding -> response
- redirect :  jsp 요청 -> jsp response -> 다른 jsp요청 -> 다른 jsp 응답



