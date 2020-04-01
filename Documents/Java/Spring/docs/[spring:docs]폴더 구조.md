200202(일)

# [spring] 폴더 구조



```default
├── domain
|   ├── domain_model.java
|   └── repository.java
├── service
|   └── service.java
|  
└──  web
|    ├── dto 
|    |	 └── dto.java
└──  └── controller.java
```



- domain layer

  요구사항, 문제 영역

  - domain model : 실제 DB와 매칭될 클래스. Entity 클래스
  - repository : DB layer 접근자

  

- service

  controller와 DAO의 중간 영역

  순서를 보장해주는 영역



- web

  컨트롤러, 뷰 템플릿의 영역

  request / response

  - dto : request 데이터를 받음
  - controller : api요청을 받는 클래스



- config 등등도 둘 수 있음..!