200223(일)

# [spring] 04. JoinPoint와 바인드 변수



###  Joinpoint 메서드

어드바이스는 클라이언트가 호출한 비즈니스 메서드의 정보가 필요하다. 그 정보를 알 수 있도록 스프링이 제공하는 것이 **JoinPoint** 인터페이스이다.



#### JoinPoint 클래스

![image-20200223160436923](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200223160436923.png)



#### Before 어드바이스 클래스 

![image-20200223160700123](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200223160700123.png)



### Before 어드바이스 설정

![image-20200223161404760](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200223161404760.png)



어드바이스별로 설정이 다르지만, 그건 차차 필요할 때 해봐야지..