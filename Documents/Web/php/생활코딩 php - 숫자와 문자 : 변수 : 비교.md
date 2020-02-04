190923(월) TIL

# 생활코딩 php - 숫자와 문자 / 변수 / 비교



### 1. 숫자와 문자

```php
// 1. 숫자
echo 1;  		   // 1 출력
var_dump(1); 	 // int(1) 출력
var_dump(6.1); // foat(6.1) 출력

echo "hello"." "."world";   // hello world 출력

#, //, /**/ 주석

```

- var_dump : 데이터타입을 출력해주는 함수
- .    :  문자열을 더하는 연산자





### 2. 변수와 상수

```php
// 변수 선언
$a=1;

// 상수 선언
define('TITLE', 'PHP TUTORIAL');
echo TITLE;    // PHP TUTORIAL이 출력됨.
define('TITLE', 'JAVA')  // 에러 뜸. 
```

- 변수 선언할때 반드시 앞에 $ 붙여야 함.
- print 와 echo는 같음
- 상수는 한번 선언하면 변경 불가





### 3. 비교

- C와 비슷

