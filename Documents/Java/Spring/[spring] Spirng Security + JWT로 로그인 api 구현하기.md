200316(월)

# [spring] Spirng Security + JWT로 로그인 api 구현하기



- 로그인 api를 구현한다.
- DB에 유저 생성 시 제한된 리소스에 접근할 수 있는 ROLE 권한을 부여한다.
- SpringSecurity 설정에는 접근 제한이 필요한 리소스에 대해서 ROLE 권한을 가져야 접근이 가능하도록 설정한다.
- 권한을 가진 회원이 로그인 성공 시, 리소스에 접근할 수 있는 JWT를 발급한다.
- JWT로 회원은 권한이 필요한 api 리소스를 요청, 사용한다.







1. Build.gradle 에 dependency 추가

2. JwtTokenProvider 생성

   토큰 생성 및 유효성을 검증하는 컴포넌트

3. JwtAuthenticationFilter 생성

   Jwt 가 유효한 토큰인지 인증하기 위한 필터

4. SpringSecurity Configuration 생성

5. Custom UserDeailService 정의

6. User Entity 생성

7. UserRepository에 findById 추가

8. 로그인 예외 추가

9. 로그인 controller 추가

10. Application에 passwordEndocer bean 추가

11. UserController 추가

12. 예외처리 수정