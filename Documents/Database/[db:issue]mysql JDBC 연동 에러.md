# Mysql + Spring JDBC 연결 에러 



### 1. serverTimezone 에러



application.property 파일에 serverTimezone 을 추가해주고,

```
serverTimezone=UTC&characterEncoding=UTF-8
```



(Intellij) property - advanced의 serverTimezone에 UTC를 추가해준다.

