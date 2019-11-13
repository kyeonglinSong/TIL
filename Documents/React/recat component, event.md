191113(수)

# react - component, event



### 1. 컴포넌트

####props

Property. 컴포넌트 속성을 설정할 때 사용하는 요소.

this 키워드를 이용하여 접근한다.

- defaultProps : props의 디폴트 값을 설정한다. 
- propTypes : 입력 타입을 지정한다.
  - array, bool, func, number, string, object등..
  - isRequired : 반드시 존재해야 함.



#### state

props는 읽기 전용으로만 사용할 수 있음. state는 컴포넌트 내부에서 읽고, 업데이트 할 수 있는 값

항상 미리 기본값을 설정해야 함.

state 값은 항상 **setState()** 로만 값 업데이트 할 수 있음.

- constructor() : 컴포넌트의 생성자 메서드

  

즉, props는 부모 컴포넌트가 설정하고,  state는 컴포넌트 자체적으로 지닌 값으로 컴포넌트 내부에서 값을 업데이트 한다.







### 2. 이벤트

유저가 웹 브라우저에서 DOM 요소들과 상호작용 하는 것.

- 이벤트 사용 시 주의할 점

  - 이벤트 이름은 camelCase로 작성한다
  - 이벤트에 함수 형태의 값을 전달한다
  - DOM 요소에만 이벤트를 설정할 수 있다 

  내가 자체적으로 만든 컴포넌트에는 이벤트를 설정할 수 없다. 전달받은 props를 컴포넌트 내부의 DOM 이벤트로 설정할 수는 있다.



#### 메서드 만들기

메서드 바인딩은 생성자 메서드에서 하는것이 정석이나, 새 메서드를 만들때마다 constructor를 수정해야 해서 불편하다. 그래서 바벨의 transform-class-properties 문법을 사용할 수도 있다.



```javascript
// 이런 코드가

		constructor(props) {
      super(props);
      this.handleChange = this.handleChange.bind(this);
    }

    handleChange(e) {
        this.setState({
            message: e.target.value
        })
    }



// transform-class-properties 사용하면 이렇게!

handleChange = (e) => {
        this.setState({
            message: e.target.value
        })
    }
```





#### input 여러 개 핸들링

event 객체를 활용하면 하나의 메서드로 여러 개 인풋을 핸들링 할 수 있다.

e.target.name 값을 사용하면 된다.

```javascript
this.setState({
  [e.target.name]: e.target.value
});

// [] 안의 값을 key 값으로 사용한다. 괄호가 없으면 오류가 발생한다!
```

