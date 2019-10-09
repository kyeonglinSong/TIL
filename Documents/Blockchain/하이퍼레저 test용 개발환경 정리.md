191008(수)

# 하이퍼레저 테스트용 개발환경 정리



### 1. Node.js



구글 크롬의 자바스크립트 엔진에 기반하여 만들어진 sever-side-platform. 즉 자바스크립트로 구현된 서버사이드 언어이다.  

node는 웹서버가 아니다(!) 노드는 그저 코드를 실행하는 방법일 뿐, 라이브러리의 도움을 받으며 HTTP 서버는 직접 작성해야 한다.



- node.js의 특징
  - 비동기  i/o처리
  - 이벤트 위주
  - 빠른 속도
  - 단일 쓰레드

  -> 뛰어난 확장성

즉 입출력이 잦고, 데이터를 실시간으로 다루고,SPA 어플리케이션이거나, json API를 기반으로 하는 어플리케이션에 사용하기 적합함. (~~완전 블록체인용이네..~~)







### 2. npm

Node Packaged Modules.  

자바스크립트를 위한 패키지 매니저. Node.js의 기본 패키지 매니저이다. Node.js로 만들어진 모듈을 인터넷에서 받아서 설치해준다. (node.js와 뗄레야 뗄 수 없다.)  

노드의 모듈의 개수는 아주아주아주 많음. 그래서 새로 만들지 않고 npm으로 설치해서 가져다 쓰는게 좋음. npm을 사용하면 node.js 버전 관리도 쉬워진다.



#### 대표적으로 사용할 npm 모듈

- Express

```bash
npm install express
```

node.js 상에서 동작하는 웹 개발 프레임워크이다. node.js의 실질적인 표준 프레임워크. 자바의 spring 프레임워크와 비슷하다.  







### 3. curl

서버와 통신할 수 있는 커맨드 명령어 툴. 웹 개발에 많이 사용되고 있는 오픈소스. 다양한 프로토콜들을 지원하고 SSL 인증방식도 가능하다.  



- Curl에서 설정 가능한 옵션들 (알아두면 유용)
  - -X : 사용할 방식 메소드 선택하기
  - -d : 함께 전달할 파라미터값 설정하기
  - -G : 전송할 사이트 url 및 ip 주소
  - -H : 헤더 정보를 전달하기
  - -i : 사이트의 Header 정보만 가져오기
  - -I : 사이트의 Header와 바디 정보를 함께 가져오기
  - -u : 사용자 정보

  

~~사실 cmd에서 직접 사용하다보면 오타도 많이나고 힘들다. 그러니까 그냥 postman 써야지~~







### 4.  go언어

구글이 개발한 프로그래밍 언어. 문법은 대체로 C와 비슷함. 하이퍼레저에서 체인코드를 작성할때 사용한다.

- http://golang.site  : go 공부하기 좋은 사이트

- Hello world 출력 코드

```go
package main
import "fmt"

func main() {
    fmt.Println("Hello World")
}
```

~~어디가 C랑 비슷한건지..~~







### 5. Docker, Docker-compose

도커는 중요해서 따로 정리했음.  document/Docker/docker란? 문서 참조하기.







###6. Hyperledger Fabric image

테스트용(+예제 진행)으로 사용할 생각이여서 hyperledger fabric 깃허브에서 제공하는 이미지 사용. 반드시 최신 릴리즈 버전으로 클론해서 사용하기



- hyperledger fabric sample 깃허브 주소 : https://github.com/hyperledger/fabric-samples

  

