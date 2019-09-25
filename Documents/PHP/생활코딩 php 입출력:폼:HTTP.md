190925(수)



# 생활코딩 php - 입출력+폼+HTTP



### 1. 입출력

```php
<?php
  echo 'Welcome,'.$_GET['id'];
?>
```



- php 앱은 url을 통해서 데이터를 입력 받을 수 있다.
- 유저랑 상호작용하는 앱이 되었다!



```
http://localhost/firstapp/io.php?name=kl
http://localhost/firstapp/io.php?name=kl&password=1111
```

- io.php 까지는 주소
- 그 뒤는 입력 데이터
- ?, =, & : 구분자
  - ? : 주소와 입력 데이터의 구분자
  - = : 이름과 값 사이의 구분자
  - & : 값과 값을 구분하는 구분자
- .  은 문자열 결합에 사용됨







### 2. HTML 폼(form)

- php 파일

```php
<?php
  echo $_GET['id'].','.$_GET['password'];
?>
```

- Html 파일

```php+HTML
<html>
  <body>
    <form method="get" action="io.php">
      id : <input type="text" name="id" />
      password : <input type="text" name="password" />
      <input type="submit">
    </form>
  </body>
</html>
```

- form : 사용자가 입력한 정보를 받아 서버로 전송하기 위한 html의 태그
- 입력 컨트롤 : 사용자가 입력한 정보를 받는 UI

- submit을 누르면 action에 지정된 url로 전송된다.





### 3. GET vs POST

- GET : url에 데이터를 첨부해서 전송하는 방식
- POST : HTTP 메세지의 본문에 데이터를 포함해서 전송하는 방식