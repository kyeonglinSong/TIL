200126

# create-react-app 에서 src가 생성되지 않을 때

public, src,and scripts folder not created while installing react-app #8088

https://github.com/facebook/create-react-app/issues/8088



```bash
$ npm rm -g create-react-app
$ npm install -g create-react-app
$ npx create-react-app my-app
```

- 에러 뜨면 sudo



라고 해결책이 나와있지만, 첫번째부터 안된다ㅜㅠ

이전 버전이 문제인 듯 해서 지우고 새로 깔아야 할 것 같은데 저 명령어로 지워지지 않는다.

-> 두 번째 줄을 실행했을 때 **already exist** 라고 나옴





**그래서,**

->  `/usr/local/bin/`  경로로 가서 직접 create-react-app 폴더를 지웠음

`$ rm create-react-app`

-> 그 후 두번째줄부터 다시 실행

-> 

![image-20200126122101420](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200126122101420.png)

실행 완료 후 이런 내용까지 뜨면 성공!!