# 스프링 IoC



1. IoC

제어권 역전

객체를 직접 생성하는게 아니라, 생성자를 통해 의존성을 받아옴.

의존성 관리를 자신이 아닌 누군가가 함

의존성 주는걸 DI 라고 한다.





bean :스프링이 관리하는 객체



2. IoC 컨테이너

 IoC 컨테이너 :  빈을 만들고 빈들사이의 의존성을 엮어주고 빈들을 제공해준다.

(빈...)

BeanFactory

--controller, --repository는 컨테이너에 빈 객체로 등록되어있음.

클래스 왼쪽 초록 콩이 있으면 빈 객체ㅋㅋ...

그리고 어노테이션(@)이나 특정 인터페이스 상속으로 알 수 있음.

직접 빈 등록도 가능