191013(일)

# Go 간단한 문법 정리

예제로 배우는 Go 프로그래밍(http://golang.site)을 보고 정리



### 1. 기본 구조

```go
func main() {
	println("Hello World")
}
```

- go는 함수형 언어이다.
- Python 문법이랑 비슷해보인다.





###2. 변수와 상수

```go
	var a int
	var b intvar f float32 =11. // 11.0 을 할당함
	var c, d, e int = 1, 2, 3

	const c int =10
	const s string = "Hi"
	const (
		apple = "apple"
		peach = "peach"
		con = "con"
	)
	const (
		apple = iota // 0
		peach        // 1
		con          // 2
	)
```

- 변수명 타입 순서로 변수를 선언한다.
- const() 안에 순서대로 상수를 선언할 수도 있다.
- 상수 값에 iota를 주면 그 값은 0, 그 다음 상수부터는 순서대로 1씩 증가된 값을 부여받는다.





###3. 데이터 타입

```go
bool a

string b // 한번 생성되면 수정할 수 없는 타입

int int32 int64
uint uint32 ...

float32 float64
complex64 complex128 // 복소수 타입

byte // uint8과 동일. 바이트 코드에 사용
rune // int32와 동일. 유니코드 코드포인트에 사용

```

- 문자열은 ''와 ""를 모두 사용 가능하다
- 문자열 안에 \n이 있어도 newLine으로 해석되지 않는다.





### 4. 포인터

- c++과 마찬가지로 &, *를 사용할 수 있다.