200223(일)

# [Spring] 06~07. 비즈니스 컴포넌트 실습



### 1. BoardService 컴포넌트 구조

일반적으로 비즈니스 컴포넌트는 네 개의 java 파일로 구성됨.

각 자바파일을 작성하는 순서와 이름 규칙도 정해져있는 편.

BoardService

- BoardVO
- BoardDAO
- BoardService
- BoardServiceImpl





### 2. BoardService 컴포넌트 작성

#### Value Object(VO) 클래스

레이어와 레이어 사이 관련된 데이터를 한꺼번에 주고받을 목적으로 사용하는 클래스. DTO(Data Transfer Object) 라고도 하는데 대충 비슷한 의미라고 보면 된다.

Q. toString() 메서드는 왜 있을까?

A. 나중에 VO 객체 값을 출력할 때 사용한다.



#### DAO(Data Access Object) 클래스 작성

데이터베이스 연동을 담당하는 클래스.  CRUD가 구현되어야 한다. DB 연동도 필요함.

1. JDBCUtil 클래스

   일단 데이터베이스 연동을 JDBC로 할 것이므로 DAO 에서 공동으로 사용할 **JDBCUtil** 클래스가 필요하다.

   JDBC 클래스는 커넥션 획득/해제 작업을 한다. (흑흑 너무 길다..)

2. DAO 클래스를 작성한다.

   **DAO  클래스의 역할**

- BoardVO 객체를 매개변수와 리턴타입으로 사용한다.
- BOARD 테이블과 CRUD 기능을 처리한다.



#### Service 인터페이스 + Service 구현 클래스 작성



###3. BoardService 컴포넌트 테스트

#### 스프링 설정파일 수정

component-scan 설정 수정





### 4. UserService 컴포넌트 구조

### 5. UserService 컴포넌트 작성

###6. UserService 컴포넌트 테스트

### 7. 어노테이션 적용





