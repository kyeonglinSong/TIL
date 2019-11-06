191103(일)

# express로 웹 서버 만들기

### express

간단한 코드로 웹 서버의 기능을 구현할 수 있다.

미들웨어와 라우터를 제공한다

```javascript
set(name, value) // 서버 설정을 위한 속성 지정. (웹서버 환경설정)
get(name) // 지정된 속성을 꺼내옴
use([path,] function[]) // 미들웨어 함수를 사용함
get([path,] function) // 특정 패스로 요청된 정보를 처리
```





### express를 사용해서 웹 서버 만들기



#### 1. 개발 폴더 만들기

#### 2. package.json 파일 생성하기

```bash
$ npm init
```



#### 3. app.js 파일 만들기

- app.js : 익스프레스의 시작점이 되는 파일
- express, http 모듈을 불러올 때 ./ 기호를 사용하지 않는 이유 : 내장 모듈이나 npm으로 설치한 모듈은 상대 패스가 아님 이름만 지정되도록 설정되었기 때문에.



express 모듈을 사용할 때에는 항상 http 모듈도 같이 불러와야 한다.



#### 4. express 모듈 설치 (없다면)

```bash
$ npm install express --save
```



이제부터 서버 실행할 수 있음. 그러나 응답이 지정되지 않아서 아무런 응답이 없음.





### 미들웨어와 라우터

#### 미들웨어

노드에서는 미들웨어를 사용하여 필요한 기능들을 순차적으로 실행할 수 있음.

익스프레스는 **web request / response**에 관한 정보를 사용하여 필요한 처리를 진행할 수 있도록 독립된 함수로 분리한다. 이 분리한 것들을 미들웨어라고 부른다.

어떤 기능의 함수를 만든 후 **use()** 메소드를 사용하여 미들웨어로 등록해 두면 클라이언트 요청을 처리할 수 있다.

각 미들웨어는 **next()** 메소드를 호출하여 그다음 미들웨어를 위해 순서를 넘길 수 있다.



#### static 미들웨어

특정 폴더의 파일들을 특정 패스로 접근할 수 있도록 해준다.

외장 모듈이므로 npm으로 설치가 필요하다.

```bash
$ npm install serve-static --save
```



#### body-parser 미들웨어

POST로 요청했을 때 요청 파라미터를 확인할 수 있도록 만들어둔 미들웨어.

GET 방식으로 요청했을 때는 **주소 문자열에 query string(요청 파라미터)이 들어간다**. 하지만 POST 방식으로 요청했을 때는 **body 영역에 쿼리스트링이 들어있게 되므로** 파싱 방법이 GET과 달라진다.





#### 라우터

라우터는 클라이언트의 request path를 보고 이 요청 정보를 처리할 수 있는 곳으로 기능을 전달해 주는 역할을 한다. (= routing)

즉, 클라이언트의 request path를 보고 각각을 담담하는 함수로 분리시킴.



```javascript
var router = express.router() // 로 라우터 객체 사용

get() // get방식 처리
post() // post방식 처리
put() // put방식 처리
delete() // delete방식 처리
all() // 모든 요청 방식 처리
```





### 익스프레스의 요청 객체와 응답 객체

```javascript
send({}) // 클라이언트에게 응답 데이터를 보냄. JSON형식으로 보낼수도 있음.
status
sendStatus
redirect // 다른 페이지로 갈 수 있음
render
```





### 쿠키와 세션

- 쿠키 : 클라이언트 웹 브라우저에 저장되는 정보. 일정 기간 동안 저장하고 싶을 때 사용한다.
- 세션 : 서버 쪽에서 상태 정보를 저장하는 역할.



#### 쿠키 처리하기

express의 **cookie-parser 미들웨어** 를 사용하면 쿠키를 설정/확인 할 수 있다.

```bash
$ npm install cookie-parser --save
```



쿠키를 사용하면 개발자 도구에서 쿠키를 확인할 수 있다.

```javascript
app.use(cookieParser());
```





#### 세션 처리하기

