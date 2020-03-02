

200302(월)

#[spring] 01. Mybatis 프레임워크 시작하기



###1. Mybatis

원래 apach에서 Ibatis 라는 이름의 프레임워크였으나, Google로 넘어가며 이름이 Mybatis로 바뀌었다.



####Mybatis 프레임워크의 특징

- 짧은 자바 코드로 DB연동을 처리한다.
- SQL 명령어를 자바 코드에서 분리하여 XML 파일에서 관리한다.



#### SQL Mapper XML 파일 작성

 이 xml 파일에 DB연동에 필요한 SQL 명령어들이 작성된다.



####Mybatis 환경설정 파일

- db.properties

  ![image-20200303004001494](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200303004001494.png)





- Sql-map-config.xml

![image-20200303003926189](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200303003926189.png)

####

#### sqlSession 객체 생성하기

![image-20200303004419520](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200303004419520.png)

- Sql-map-config.xml 파일로부터 설정 정보를 읽어들일 **입력 스트림을 생성**한다.
- 입력 스트림을 통해 파일을 읽어 **sqlSessionFactory 객체를 생성**한다.





####DAO 클래스 작성

- Mybatis 를 이용하여 DB 연동을 처리한다.