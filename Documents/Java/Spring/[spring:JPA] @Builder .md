

#[spring/JPA] @Builder 



####JPA 엔티티에 Builder annotation을 사용하는 이유

- 인자가 많을 경우 쉽고 안전하게 객체 생성을 할 수 있다.
- 인자의 순서에 구애받지 않는다.





클래스 위에 @Builder를 사용 시 @AllArgsConstructor 어노테이션을 붙인 효과를 발생시켜 **모든 멤버 필드에 대해서 매개변수를 받는 기본 생성자를 만든다.**



따라서 받아야 하는 생성자를 필요조건에 따라 지정하고 그 위에 @Builder를 붙이는 것이 좋다.



[참고 : https://github.com/cheese10yun/blog-sample/tree/master/lombok]