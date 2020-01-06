200106(월)

# git pull request

#### (pull request를 보낸 상대에게) 내가 수정한 코드를 검토한 후에 원본 코드에 merge 해주세요



(ex)

### (1) pull request 보내는 사람

#### 1. 원본 코드 클론 + 코드 작업

```
$ git clone (url)
```

그 후 내 로컬에서 코드 작업



####2.  브랜치 새로 파기

```
$ git checkout -b example
```



####3. 판 브랜치에 수정한 코드 올리기

```
$ git add .
$ git commt -m "메세지"
$ git push
```



####4. Pull request 보내기

깃허브에서 pull request 버튼으로 보내는 브랜치, 받는 사람을 지정한다.



###(2) pull request 받는 사람

#### 4. 코드 변경내용 확인하기 

이 코드를 원본 코드에 merge 해도 될지 결정하기



####5. 동기화 및 branch삭제

```
$ git pull
$ git branch -d example (브랜치 삭제)
```



