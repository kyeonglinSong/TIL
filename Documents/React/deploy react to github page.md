200127(월)

# react github page에 deploy

#### 1. public/index.html 의 title 변경

​	원래는 React App

#### 2. npm install gh-pages

####3. package.json 설정 

​	"homepage": "https://username.github.io/repo이름" 만들기

​	"scripts" 안에 "deploy": "gh-pages -d build "

​	"scripts" 안에 "predeploy": "npm run build"

####4. npm run deploy

​	deploy는 predeploy를 호출

​	컴파일 완료! 

#### 5. github page가 Publish 됨!



코드에 변경사항이 있을때마다 deploy 다시 해야함!

