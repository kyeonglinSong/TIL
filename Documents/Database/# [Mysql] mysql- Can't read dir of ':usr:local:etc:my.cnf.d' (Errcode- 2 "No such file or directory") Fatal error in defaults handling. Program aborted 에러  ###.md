200503(일)

# [Mysql] mysql: Can't read dir of '/usr/local/etc/my.cnf.d' (Errcode: 2 "No such file or directory") Fatal error in defaults handling. Program aborted 에러

###문제

터미널에서 `mysql -u root -p` 를 치면  위 제목과 같은 에러가 발생한다.



### 해결

``` bash
$ mkdir /usr/local/etc/my.cnf.d
```

파일 위치가 문제였나보다. 위 명령어를 복붙하니 바로 해결되었다.