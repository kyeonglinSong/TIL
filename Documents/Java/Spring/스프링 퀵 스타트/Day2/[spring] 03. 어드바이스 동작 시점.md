200223(일)

# [spring] 03. 어드바이스 동작 시점



#### Before 어드바이스

포인트컷으로 지정된 메서드가 실행되기 전에 동작한다.



#### After Returning 어드바이스

포인트컷으로 지정된 메서드가 실행된 후 수행 결과(데이터)를 리턴하는 시점에서 동작한다.



#### After Throwing 어드바이스

포인트컷으로 지정된 메서드가 실행되는 중 예외가 발생하는 경우 동작한다.

예외가 발생하지 않는 경우에는 동작하지 않는다.



#### After 어드바이스

포인트컷으로 지정된 메서드가 실행된 후 예외 발생여부와 관계없이 동작한다. (finally 블록 같음)



#### Around 어드바이스

클라이언트의 메서드 호출을 가로챈다. 그래서 메서드 실행 전과 후에 두 번 동작한다.

