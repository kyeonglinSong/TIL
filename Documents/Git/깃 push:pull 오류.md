#Git push/pull 오류..



### 1. Push오류

- fetch- first 가 뜨는 경우

```
git fetch remote이름 저장소이름
```

- fetch를 했는데도 non-fast-forward 가 뜨는 경우
  - 현재 repository가 서버의 repository보다 오래되었기 때문

```
git pull 후 다시 git push
```





###2. Pull 오류

- pull을 하면 local에 자동으로 최신 내용들이 merge된다.



- pull 할 때 non-fast-forward가 뜨는 경우

```
뒤에 --allow-unrelated-histories 를 붙이기
```

