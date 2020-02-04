# 파이썬 버전 다운그레이드 and 업그레이드 하는 법

하이퍼레저 하느라 python 2.7로 다운그레이드 시켜야하는데 얼마나 힘들었는지..ㅠㅠ



파이썬 2.x와 파이썬 3.x가 모두 깔려있다는 전제 하에,

###python 2.x -> python 3.x 업그레이드

```bash
$ brew switch python 3.x.x
```



### python 3.x -> python  2.x 다운그레이드

```bash
$ brew unlink python
```

