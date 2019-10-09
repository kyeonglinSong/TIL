191009(수)

# SPA, REST, RESTFUL APP



### 1. SPA란? 

single page application

단순하게 말하면 페이지가 한개인 어플리케이션. 즉 HTML 파일은 한 번만 전송되고, 대신 JSON 이나 XML같은 데이터만 서버로부터 요청-전송된다.





### 2. REST

Representational State Transfer

sw 프로그램 개발 아키텍처의 형식 중 하나. 자원을 이름으로 구분하고 해당 자원의 상태를 주고 받는 것. 일반적으로는 HTTP(URL)를 통해 CRUD를 실행하는 API를 뜻한다.



- REST를 정의하기 위한 조건들
  - client-server 구조
  - stateless : 서버는 각 요청을 완전히 별개의 것으로 인식하고 처리. 이전 요청이 다음 요청의 처리에 연관되어서는 안된다.
  - cacheable
  - layered system
  - 인터페이스의 일관성





### 3. RESTful

REST의 가이드라인. 공식적이진 않고 그냥 모두가 암묵적으로 합의한 방식

