191113(수)

# React 개발환경 구성

### 1. Node.js +  npm

node.js 프론트엔드 개발용으로 공부하는 중이라서 이미 깔려있다.



### 2. nvm

### 2. Nvm

macOS와 Ubuntu에서 node.js 버전 관리해주는 도구



### 3. yarn

패키지 관리자 도구. 

npm은 의존하는 라이브러리 개수가 많아지면 속도가 낮아지고, 의존하는 버전이 설치되는 시점을 기준으로 결정한다.

즉, npm을 대체할 수 있는 패키지 매니저이다.



```bash
$ brew install
$ brew install yarn
$ echo 'export PATH="$(yarn global bin):$PATH"' >> ~/.bash_profile
```



### 4. VS Code + 확장 프로그램

Vs code는 깔려있음. 확장 프로그램만 설치하면 됨.

