200223(일)

#[spring] 스프링 AOP

비즈니스 컴포넌트 개발에서 가장 중요한 원칙 두가지

- 낮은 결합도 -> DI
- 높은 응집도 -> AOP



### 1. AOP 이해하기

**관심 분리 (Seperation of Concerns)**

- **횡단 관심(Crosscutting Concerns)** : 메서드마다 공통으로 등장하는 로깅, 예외, 트랜잭션 처리를

- **핵심 관심(Core Concerns) ** : 비즈니스 로직

두 관심을 분리하면 응집도가 올라간다.



기존 OOP는 완벽한 관심 분리가 어려움.

-> ServiceImpl 클래스와 LogAdvice 객체가 강한 결합을 가지고 있음.

![image-20200223145522172](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200223145522172.png)

이렇게 클래스를 작성해서 ServiceImpl 클래스에 일일이 삽입해야 한다.





### 2. AOP 시작하기

1. pom.xml에 AOP 라이브러리 추가

![image-20200223150132992](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200223150132992.png)



2. applicationContext.xml 에 네임스페이스 추가

![image-20200223150342471](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200223150342471.png)

![image-20200223151145151](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200223151145151.png)

​																		~~(아직 뭔말인지 모르겠다..)~~



이젠 Log 클래스를 변경하고 싶으면 applicationContext.xml만 변경하면 된다!

-> <u>횡단 관심 메서드와 핵심 관심 메서드의 소스 결합이 없다.</u>

