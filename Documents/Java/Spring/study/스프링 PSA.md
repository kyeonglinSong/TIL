200104(토)

# 스프링 PSA

### PSA : Portable Service Abstraction

보통 service abstraction이라고 부름



#### PSA란

서블릿 애플리케이션을 만듦에도 불구하고 서블릿을 사용하지 않음.



보통 서블릿 프로그래밍을 하면,

http서블릿을 상속받아서.. 겟요청 들어오면 doGet.. 이런식으로 오버라이딩해서 요청 처리하고 서블릿을 web.xml에 매핑해서 특정 요청이 들어오면 처리.. 뭐 이런거... 이렇게..



하지만 스프링은!

@GetMapping 등 추상화된 어노테이션을 사용해서 처리한다! 추상화를 사용하면 코딩하기 편하다.



스프링 MVC

@controller : 요청을 매핑할 수 있는 컨트롤러 클래스가 됨.

@getMapping @PostMapping 사용가능

- c : controller
- m : model
- v : view : 뷰 이름을 리턴하는데, 뷰는 src/main/resources/template에 있음



####PSA의 장점

- 서블릿을 low-level로 안써도 되고 매핑도 쉬움

- 서블릿 코딩 / 리액티브 코딩. 

  코드는 변경하지 않고 서버를 톰캣 제티 네티 아무거나 쓸 수 있음!

