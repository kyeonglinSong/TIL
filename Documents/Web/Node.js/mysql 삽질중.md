191119(화)

# MYSQL 삽질중



### 1. Pk 자동증가...!!

```mysql
NOT NULL AUTO_INCREMENT PRIMARY KEY를 붙여놓고

INSERT INTO TABLENAME(이곳에 id 빼고 칼럼명 다 넣기) VALUES();
하면 된다!
```





### 2. FK의 조건

바보같이 계속 pk가 아닌 애를 FK로 참조하려고 했었다..

pk를 참조해야 함! 참조하는 테이블에서 참조하고 싶은 column을 pk로 설정해두어야함.

