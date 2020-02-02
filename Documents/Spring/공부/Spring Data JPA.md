# JPA로 DB 다루기



####JPA : 자바 표준 ORM

객체지향과 관계형 데이터베이스의 중간에서 패러다임을 일치시켜주는 기술

Sql 종속적인 개발을 하지 않아도 된다.

- ORM : 객체를 매핑 / SQL Mapper : 쿼리를 매핑



### Spring Data JPA

JPA는 인터페이스로써 자바 표준명세서임. 사용하기 위해서는 구현체가 필요함. (ex. Hibernate)

구현체를 쉽게 사용하기 위해서 **추상화시킨 모듈**이 spring data JPA

- JPA <- Hibernate <- Spring Data JPA



hibernate를 사용하는 것과 spring data jpa를 사용하는 것은 별 차이가 없지만 **구현체/저장소 교체의 용이성** 때문에 spring data jpa를 권장함.



#### JPA를 사용하는게 왜 좋을까?

- CRUD 쿼리 직접 작성 안해도 됨
- 속도 이슈도 딱히 없음



---



###프로젝트에 spring data JPA 적용하기



1. build.gradle에 의존성 등록



2. 도메인 패키지 만들기 / Entity 클래스 만들기

- 도메인 : sw 요구사항 혹은 문제 영역
- Entity :  테이블과 링크될 클래스



3. JpaRepository 인터페이스 생성

- JpaRepository : 위에 만든 클래스로 DB 접근을 위한 인터페이스
- Miabits에서는 DAO라고 불리는 DB layer 접근자. JPA에서는 repository라고 부르며 인터페이스로 생성한다.
- JpaRepository를 상속하면 기본적인 CRUD 메소드가 자동으로 생성된다.

**!! Entity 클래스와 entity repository는 함께 위치해야 한다.**



#### jpa annotation

- @Entity :  테이블과 링크될 클래스
- @Id : pk
- @GnenratedValue : pk 생성규칙
- @Column : 사실 안써도 되는데, 기본값 이외 옵션 변경이 필요할 때 사용함.



####TIP

- Entity의 pk는 Long 타입의 auto.increment를 사용하는게 좋음.
- Entity 클래스에서는 절대 Setter 메소드를 만들지 않음!
  - Setter 메소드가 없으면 생성자를 통해 최종값을 채운 후 DB에 삽입함.
  - @Builder를 통해 제공되는 빌더클래스로 값을 채워줌.







