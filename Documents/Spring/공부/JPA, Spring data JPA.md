191229(일)

# JPA, 스프링 데이터 JPA

### 1. JPA (Java Persistence API)

- 현재 자바 ORM의 기술 표준. 인터페이스의 모음
- JPA 인터페이스를 구현한 대표적인 오픈소스가 Hibernate,
- JPA는 애플리케이션과 JDBC 사이에서 동작한다.
  - 개발자가 JPA를 사용하면, JPA는 내부에서 JDBC API를 사용하여 SQL을 통해 DB와 통신한다.



### 2. Spring data JPA

- 스프링 프레임워크에서 JPA를 편리하게 사용할 수 있도록 제공해주는 프로젝트

  - CRUD를 위한 인터페이스
  - 쿼리 메소드
  - 파라미터 바인딩

  