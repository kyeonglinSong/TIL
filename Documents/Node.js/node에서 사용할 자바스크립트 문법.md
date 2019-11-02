191102(토)

# node에서 사용할 Javascript 문법



### 대표적인 전역 객체

- console : 콘솔 창에 결과를 보여주는 객체
- process : 프로세스의 실행에 대한 정보를 다루는 객체
- exports : 모듈을 다루는 객체



### console 메소드

```javascript
dir() // 자바스크립트 객체의 속성들을 출력한다
time(id) // 시작 시간 측정
timeEnd(id) // 끝 시간 측정
// timeEnd 부분에서 id : 시간 을 출력한다.
```





### JSON

``` javascript
{"key", "value"}
```

자바스크립트 객체 포멧으로, 단말끼리 데이터를 주고받을 때 사용한다.

python dictionary와 형식이 같은듯





### 내장 모듈

- os : 시스템 정보를 알려주는 모듈

```javascript
hostname()
totalmem()
networkInterface()
...
```



- path : 파일 패스를 다루는 모듈

```javascript
join() // 여러 개의 파일을 합쳐 하나의 파일 패스로 만들어준다.
dirname() // 디렉터리 이름 반환
basename() // 확장자를 제외한 이름 반환
extname() // 확장자 이름 반환
```





### 주소 문자열 & 요청 파라미터 모듈

- Url 모듈

```javascript
parse() // 주모 문자열을 파싱하여 URL객체로 만들어준다.
format() // url 객체를 주소 문자열로 반환한다.
```



- querystring 모듈 

요청 파라미터는 &기호로 구분된다. querystring 모듈은 요청 파라미터를 쉽게 분리할 수 있게 해준다.

```javascript
parse() // 요청 파라미터 문자열을 파싱하여 요청 파라미터 객체로 만들어준다.
stringify() // 요청 파라미터 객체를 문자열로 반환해준다.
```





### 이벤트

- EventEmitter 클래스

```javascript
on(event, listener) // 지정된 이벤트의 리스너를 추가
once(event, listener) // 지정된 이벤트의 리스너를 추가, 그러나 한 번 실행 후에 자동으로 리스너를 제거
removeListener(event, listener) // 리스너를 제거
```

 

- process 객체 : 노드에서 언제든지 사용할 수 있는 객체