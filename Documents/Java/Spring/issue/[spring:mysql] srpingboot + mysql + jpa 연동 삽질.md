200214

#[spring] srpingboot + mysql + jpa 연동 삽질

### 목표 : 스프링부트와 mysql과 jpa(hybernate)를 연동해보자



###상황 : 

1. 스프링에 mysql 연동은 클리어~
2. 그러나 Dto테스트가 안돌아감.. 에러뜸~.~



### 확인해볼 것 들 : 

- `build.gradle` 의` compile('org.springframework.boot:spring-boot-starter-data-jpa')` 확인하기
- 여기 버전에 따라서 `application.properties`의 `spring.datasource.driverClassName` 과 `spring.datasource.url` 을 확인해야함~~
- mysql 버전때문인것 같은데..  아무튼 연동한 mysql의 버전에 맞추어서 해야하는듯!

