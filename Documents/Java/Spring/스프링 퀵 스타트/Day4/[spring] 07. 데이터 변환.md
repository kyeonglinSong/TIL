200229(토)

# [spring] 07. 데이터 변환 - JSON



### 1. JSON 으로 변환하기

VO 객체에 저장된 데이터를 JSON 형식으로 변환하자!



#### (1) Jackson2 라이브러리 내려받기

- Pom.xml에 디펜던시 추가

![image-20200301005008420](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200301005008420.png)



#### (2) HttpMessageConverter 등록

Response 결과를 HTML이 아닌 JSON이나 XML로 변환하려 메세지 body에 저장하려면 **Converter**를 사용해야 한다.



- Presentation-layer.xml에 mvc:annotation-driven 추가

![image-20200301005240077](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200301005240077.png)



#### (3) 링크 추가

- JSON 형태로 글 목록을 요청할 수 있도록 index.jsp 파일에 링크 추가

![image-20200301005400510](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200301005400510.png)



#### (4) Controller 수정

![image-20200301010848812](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200301010848812.png)

어디서 많이 본 모양이다... ~~나중에 써먹자.~~



####(+) 결과화면

![image-20200301010951465](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200301010951465.png)

잘 나온다!