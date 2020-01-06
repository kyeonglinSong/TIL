# Mysql JDBC 연결 에러 





### 1. serverTimezone 에러



application.property 파일에 serverTimezone 을 추가해주고,

```
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/test?serverTimezone=UTC&characterEncoding=UTF-8
```



property - advanced의 serverTimezone에 UTC를 추가해준다.