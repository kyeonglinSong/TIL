#[spring] 스프링 부트 테스트



- spring-boot-test

- spring-boot-test-autoconfigure : 테스트 관련 자동 설정 기능 제공



보통은 spring-boot-starter-test 로 두 모듈을 함께 사용한다.



스프링부트는 각종 테스트를 위한 어노테이션을 제공한다.

@SpringBootTest

@WebMvcTest

@DataJpaTest

@RestClientTest

@JsonTest





### @SpringBootTest

통합 테스트를 제공하는 기본적인 테스트 어노테이션.

애플리케이션이 실행될 때의 설정을 임의로 바꾸어 테스트를 진행할 수 있다.

여러 유닛테스트를 합친 통합 테스트를 수행할 때 적합하다.



 기본 제공되는 테스트코드

애플리케이션 컨텍스트를 로드하여 테스트를 진행한다.



@RunWith()

JUnit에 내장된 러너 대신 어노테이션에 정의된 러너 클래스를 사용한다.



ㅇ