200129(수)

#REST API 만들기

####1. application.java

 @SpringBootApplication 이 붙은 클래스

스프링부트의 자동 설정, 스프링 Bean 읽기와 생성을 모두 자동으로 설정된다.

항상 프로젝트 최상단에 위치해야 함.



(스프링부트는 내장 WAS가 있어서 서버에 톰캣을 설치할 필요 없이 스프링부트로 만들어진 Jar 파일로 실행하면 된다.)



@RestController : JSON을 반환하는 컨트롤러로 만들어준다.

@GetMapping : http get요청을 받을 수 있는 API를 만들어준다

@RequestParam : 외부에서 api로 넘긴 파라미터를 가져오는 어노테이션ㄹ