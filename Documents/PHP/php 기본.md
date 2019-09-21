190921 TIL

# PHP 기본 (생활코딩)



### 1. php란?

PHP : Hypertext Preprocessor

* hypertext : 문서와 문서가 링크로 연결되어있는 구조

server side script (= server side tech)

초창기에는 perl로 작성 -> 현재는 C

웹 개발에서 가장 많이 사용되는 언어중 하나

HTML을 동적으로 생성해주고 데이터베이스와 상호작용한다. 거의 모든 DB를 지원한다.

- PHP로 만들어진 서비스 : 위키피디아, facebook



#### 서버와 클라이언트의 차이

- 서버의 구성요소 
  - web server : Apache, IIS, nginx 
  - php, python, java 
  - mysql, oracle
- 클라이언트의 구성요소
  - WB(=web client) : chrome, ff, ie 



#### CGI

웹서버와 PHP 사이의 통신규약



#### PHP의 장점

- 웹에 최적화된 언어

- 거의 모든 호스팅 환경에서 사용 가능
- 컴파일이 필요없는 interpreter방식의 언어
- 배우기 쉽다.





### 2. PHP 설치

-  bitnami 에서 mamp 설치(apache + mysql + php)





### 3. PHP

- Bitnami - open application folder -> apache2/htdocs -> firstapp 폴더 추가

- hello.php 작성

  ```php
  <?php 
  echo "hello world";
  ?>
  ```

  - <?php : php문법이 시작됨을 알려줌
  - echo : 출력