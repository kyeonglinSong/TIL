200314(토)

#[spring] Springboot Security + OAuth2 로 사용자 인증 API 만들기

### 0. 준비

#### 일반적인 회원가입 + 인증 개발 방식 2가지

1. 회원가입 생성 + 생성시 아이디/비밀번호로 사용자 인증 후 권한부여

2. 회원가입 생략 -> OAuth2로 사용자 인증 후 권한 부여

   -> 구글, 카카오, 네이버 등의 인증 사용



---> **두 번째 방식을 사용**할 것임.



####사용 버전

- springboot 2
- gradle 
- mysql

- Spring security 1.5 + OAuth2 API 







###1. 프로젝트 설정

#### (1)  dependency 추가 

- **build.gradle**

![image-20200314134539378](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200314134539378.png)



- **Lombok 설정**

preference -> Build, Execution, Deployment -> Compiler -> Annotation processors -> Enable annotation processing 체크박스 체크, apply





#### (2) DB 연동

- application.properties 추가

![image-20200314135444563](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200314135444563.png)



- 위에서 적은 url, username, password, driverClassName을 사용하여 mysql에 연결



#### (3) application 추가 후 실행 테스트







### 2. Domain 생성

- 소셜미디어 타입을 가지고 있는 SocialType enum 객체 생성

  SocialType : 어떤 소셜 미디어인지 구별해주는 컬럼

  

- SocialType과 principal을 가지는 User 객체 생성

  principal : OAuth2 인증으로 제공받는 키값





### 3. 각 소셜 미디어의 개발자센터에서 Client ID, Secrete 발급받기

- Google

![image-20200314143214328](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200314143214328.png)

​																		~~뭔가 만들어졌다..!~~



- 카카오

![image-20200314143833976](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200314143833976.png)

​																		~~카카오도 뭔가 생겼다~~