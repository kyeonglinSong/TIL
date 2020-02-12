# REST API 설계 원칙



https://www.slideshare.net/Byungwook/rest-api-60505484 참고



- 대상(이하 리소스)에 대한 행동(CRUD)을 정의하는 개념

- 리소스는 복수형 명사여야 한다
- URL은 2 depth 정도만

- 에러 처리 : 상세 내용은 HTTP body에 표현

- 많은 도큐먼트를 리턴할 때는 잘라서 리턴하는 페이징 처리가 필요
  - (ex) /records?offset=100&limit=25
- 일부만 응답받는 형식 
  - (ex) /terry/friends?fields=id,name