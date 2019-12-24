# PostgreSQL이 연결이 안될때



###1. 이런 오류가 뜨면서 연결이 안될 때

psql: could not connect to server: No such file or directory. Is the server running locally and accepting connections on Unix domain socket "/tmp/.s.PGSQL.5432"?



postgres cannot access the server configuration file "/usr/local/pgsql/data/postgresql.conf": No such file or directory



#### 아래 명령어 복사/붙여넣기 하면 된다.

```bash
$ pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
```

