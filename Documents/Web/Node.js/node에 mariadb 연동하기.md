191115(금)

# node.js + mariaDB 사용하기



### 1. mariaDB 사용하기



- 설치하기

```bash
$ brew install mariadb
```



- 시작하기

```bash
$ mysql.server start
$ mysql -u 아이디 -p 스키마명
비밀번호 입력
```





### 2.  Sql 문법 대충

- insert

```sql
insert into portfolio.users
values ('kl', 'kl', 'kl@gmail.com', '03-22-1997', '010-8749-3597', '어딘가')
```

