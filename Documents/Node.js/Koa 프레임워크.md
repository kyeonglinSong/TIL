191114(목)

# koa 프레임워크

koa application은 미들웨어의 배열로 구성되어 있다.



- app.use : 미들웨어를 애플리케이션에 등록한다.

- ctx : 웹 요청과 응답 정보를 지니고 있다 

- next : 다음 미들웨어를 호출하는 함수. next를 등록하지 않으면 다음으로 넘어가지 않는다.





### 라우팅

Koa-router 모듈을 사용한다.



#### 1. 라우트의 파라미터와 쿼리 읽기

- 파라미터

: 을 사용하여 라우터 경로를 설정

있을수도 있고 없을수도 있다면 :name? 처럼 물음표를 뒤에 붙인다.

파라미터는 **ctx.params** 에서 조회할 수 있다.



- Url 쿼리

/post/?id=10

이런식으로 요청하면 **ctx.qrery**에서 조회할 수 있다. 자동으로 객체 형식으로 파싱해준다.

문자열 형태의 쿼리스트링이 필요하면 **ctx.querystring**을 사용한다.



#### 2. 컨트롤러

컨트롤러 : 라우트 처리 함수만 모아 놓은 파일

```bash
$ yarn add koa-bodyparser
```







### REST API

웹 애플리케이션을 만들려면 데이터베이스에서 정보를 r/w 해야한다.

웹 브라우저에서 직접 접속할 수 없으니 rest API를 사용함.



#### REST API의 HTTP 메서드 종류

- get : 데이터를 조회할 때 사용
- post : 데이터를 등록할 때 사용. 인증작업에도 사용
- delete : 데이터를 지울 때 사용
- put : 데이터를 새 정보로 통째로 교체할 때 사용
- patch : 데이터의 특정 필드를 수정할 때 사용