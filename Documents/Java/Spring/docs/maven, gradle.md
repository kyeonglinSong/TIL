191226(목)

# maven, gradle



### 1. Maven

프로젝트 빌드, 관리에 사용되는 도구.(빌드 툴 or 프로젝트 관리 툴) 개발자들이 전체 개발과정을 한 눈에 알아볼 수 있다.

모듈화 하기 좋다. 

멀티프로젝트에서 상속 구조.



그래들에 비해 좀더 상세한 POM파일, 프로그래밍 지식이 덜 필요함.



초보자가 이해하기 어렵다.

느리게 여겨지기도 한다.



메이븐 활용 패턴

- bulid : 소스코드를 컴파일한다. 바이너리를 생성한다.
- package : 배포 가능한 파일 생성
- test : 단위 테스트 실행
- report : 결과를 정리하고 빌드 수행 리포트를 생성
- release : 빌드 후 생성된 아티팩트를 로컬 혹은 원격 저장소에 저장(배포)한다.



POM : project object model. 프로젝트 객체 모델

프로젝트 당 하나의 pom.xml을 가진다.

pom은 프로젝트 자체와 의존성 설정 및 정보를 포함한다.

메이븐은 pom.xml을 읽어 프로젝트를 가공하는 방법을 이해한다.



CoC : convention over configuration

 메이븐의 큰 철학. 명확한 관습으로 인해서 편해진다.

즉, 개발자들의 관습으로 알고있는 디렉터리나 위치 정보를 그대로 사용하자는 거.

설정 작업이 좀 더 간결해지고 쉬워진다.





###2. Gradle

멀티프로젝트에서 주입 방식. 멀티프로젝트에 메이븐보다 적합함.