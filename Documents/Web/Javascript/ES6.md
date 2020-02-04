200123(금) - 

# ES6

자바스크립트를 좀 더 제대로! 알기 위해서 ES6 공부하기

인프런 https://www.inflearn.com/course/es6-강좌-자바스크립트# 를 보며 정리





### 0. overview

- ES6 === ES2015

- 우리나라에서는 아직 ES5를 많이 사용함. 그러나 해외에서는 거의 표준으로 사용됨

- ES6 코드 ------------(바벨)------------> ES5 코드



---



### 1. Scope

#### 1-1. let

let : 블록 안에서만 유효한 변수. 블록 밖에서 접근할 경우 error

var : 블록 바깥에서도 접근 가능한 변수.



#### 1-2. closure

이벤트 델리게이션(?..)

closure상황 : 스코프가 존재하고 콜백은 나중에 실행됨.  콜백 밖의 변수값을 참조하면 뭔가 문제가 생김.  

-> 보통은 스코프를 새로 만들어 지역변수화 시켜서 문제 해결

-> for문에 var 대신 let을 쓰면 해결! 



#### 1-3. const

원래 상수는 대문자로 작성, 컨벤션 기법으로 상수를 지정했음.

ES6는 const 키워드를 사용해 상수 지정 가능. 상수 값을 변경하려고 하면 error

배열도 const 사용 가능.



#####변수 키워드 사용 전략

- const를 기본으로 사용한다.

- 변경이 될 수 있는 변수는 let을 사용한다.

- var는 사용하지 않는다.



#### 1-4. const의 특성과 immutable array

const가 수정할 수 없음을 의미하는것은 아님! (절대 불변 x)

const를 사용하더라도 배열과 오브젝트의 값을 변경할 수 있음.

- list.push() 처럼 추가/삭제는 가능
- const는 값의 재할당 / 직접 수정을 제한!



immutable array : 객체가 생성된 이후 그 상태를 변경할 수 없는 array

const로 immutable array를 만들 수 있음.

- react에서 많이 사용하게 됨.



---



### 2. String

#### string의 새로운 메서드들

- startsWith() : 이걸로 시작하는지

- endsWith() : 이걸로 끝나는지
  - 복수인 이유(s)는 문자열도 비교 가능해서
- includes() : 이 글자가 들어있는지



---



### 3. Array

#### 3-1. for of - 순회하기

array의 값 순회하는 법 

- 기본 for문

- for in 

  -  `for(let idx in data){};`
  - for in 의 문제 : 상위 객체에 생성된것들까지 출력해줌(prototype 함수 등)
  - 따라서 for in을 array 순회에서 사용하면 안됨ㅠ.ㅠ

- forEach

  - `forEach(function(value){    });`

- for of : 

  - `for (let value of data){};`
  - for each와 for in의 실수를 줄이기 위해 for of가 새로 생김.
  - 문자열에서도 사용 가능 : 문자열을 char 단위로 순회하며 출력해줌

  

#### 3-2. spread operator

spread operator, 펼침 연산자 (...)

- `...list`

- 원 배열과 ...를 사용하여 만든 배열에 === 연산자를 사용하면 false가 나온다

  - 복사한 배열은 원 배열을 펼쳐서 만든 완전 다른 배열이다!

  

#### 3-3. spread operator의 몇가지 활용

- 배열 중간에 특정 배열 복사하기
- 함수에 parameter로 값 전달 가능



#### 3-4. from 메서드

자바스크립트에는 가변 파라미터가 들어올 경우 arguments를 사용할 수 있음(아주 권장은 아님)

argument : 배열 모양인데 배열은 아님(ㅋㅎㅎ..). 배열의 메서드 사용 못함.

메서드를 사용하려면 이런 가짜 배열을 진짜 배열로 바꿔줘야함.

- `let newArray = Array.from(arguments);`

- from을 사용하면 쉽게 가짜 배열을 진짜 배열로 만들 수 있다.



- toString.call() : 타입 반환
- innterText() : 자바스크립트로 html을 다룰 때 DOM요소 내의 내용을 조작, 문자열 그대로를 리턴함.

---



### 5. Object

#### 간단히 객체 생성하기

object literal

`return {`

​	`getName: getName,`

​	`setName: setName`

`}`

말고,

`return { getName, setName}` 이 지원된다.



---



### 5. Destructuring

#### 5-1 Destructuring Array

```javascript
let data = ["랄라", "룰루", "야호", "뭐지"];
let [kl,,kyeonglin]
// 0번째, 2번째 요소가 인덱싱 됨
```



#### 5-2. Destructuring Object

```javascript
let obj = {
  name : "kl",
  address : "somewhere",
  age : 20
}

let {name, age} = obj 
let {name:myName, age:myAge} = obj; //새 이름을 할당하여 사용할 수 있음

```



#### 5-3. Destructuring 활용 JSON 파싱

그래서 디스트럭처링을 어디다가 사용하는가? -> JSON 파싱에 활용함



#### 5-4 Destructuring 활용 Eevent 객체 활용





---



### 6. Set & WeakSet

#### 6-1. Set

`let mySet = new Set();`

중복없이 동일한 값을 저장.

이미 존재하는 값인지 체크할 때 사용하기 좋음.

- `has()` 로 체크할 수 있음



#### 6-2. WeakSet

참조를 가지고 있는 객체만 저장이 가능하다.

객체형태를 중복 없이 저장하고싶음.

`let weekset = new WeakSet()`



---



### 7. Map & WeekMap

Key / value  구조

key인 function의 카운트를 세고싶을 때.



WeekMap 활용

-  Private 변수 활용

```javascript
const wm = new WeakMap();

function func(a, b){
  wm.set(this, {a,b});
}

// 사용할 때
const {a, b} = wm.get(this);
```



----



### 9. Template

#### 9-1. template 처리

json으로 응답받음 -> js object로 변환 -> 데이터처리 조작 -> DOM에 추가

Data + HTML 문자열의 결합이 필요하기 때문에



`` 안에 변수값은 ${}안에 집어넣어서 사용.



#### 9-2. Tagged Template literals

function에서 처리를 한 후 결과값을 반환받아서 사용



---



### 10. function

#### 10-1. Arrow function의 활용

```javascript
let newArr = [1,2,3,4,5].map(function(value){
  return value*2;
});

// arrow function 활용
let newArr = [1,2,3,4,5].map( (v) => (v*2));
```





