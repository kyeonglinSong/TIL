200219(수)

# [Spring] REST API를 위한 폴더구조

미래의 나를 위한 폴더,클래스 구조 정리



스프링 API를 위해서는 크게 3개의 폴더구조, 5개의 레이어가 필요함!

- domain : DB에 맞닿아있는 레이어. @Entity들이 들어있다.
  - Entity
  - Repository
- service : 순서를 보장하는 레이어 @Transactional
  - -service 파일들
- Web
  - dto : domain을 직접 건드리는건 하드하니까, controller를 위해서 view를 위한 부분만 변경할려구~~
  - ApiController : 외부 요청을 받는 곳





#### dto

- @builder, @NoArgsConstructor
- domain이랑 비슷하다. controller가 필요한 부분만 다시 만드는 느낌





#### service

- @Service, @RequiredArgsConstructor
- 레포지토리를 하나 만든당
- @Transactional





#### ApiController

- Service 객체를 만듦
- 여기서 @-Mapping 을 사용해서 url에 매핑해준다