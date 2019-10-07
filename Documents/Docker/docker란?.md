191007(월)

# Docker

책  "Using Docker by Adrian Mouat(O'Reilly)" part 1 요약 



### 1.  컨테이너(container)

🐶 응용프로그램의 이식성과 독립성이 목정

- 호스팅 환경 가상화
- 응용프로그램 자체를 캡슐화
- 호스트 OS의 자원을 공유 -> 효율적으로 사용할 수 있게 해줌
- 이식성 제공 ("내 컴퓨터에선 잘 동작하던데!" 해결)
- 매우 가벼움 -> 여러 컨테이너 운영 가능
- 클라우드에 배포할 수 있다





### 2. 도커(docker)

- 기존 리눅스 컨테이너 기술을 차용함
- 도커 플랫폼의 두 가지 컴포넌트
  - 도커 엔진 : 컨테이너 생성 / 실행
  - 도커 허브 : 컨테이너 배포를 위한 클라우드 서비스 제공



- 도커 엔진
  - 컨테이너 운영을 위한 빠르고 간편한 인터페이스 제공
  - 오픈소스화 됨
- 도커 허브
  - 다수의 컨테이너 이미지 제공 
- 그 외 Swarm(클러스터링 관리자), 카이트매틱(GUI), Machine(호스트 생성 명령 유틸리티) 등의 도구도 제공된다.

- 이미지
  - 컨테이너 실행에 필요한 파일과 설정값들을 포함하고 있는 것
  - 이미지로 만들기 -> 가상머신 스냅샷 찍는것과 비슷







### 3. 첫 번째 이미지 실행하기



```bash
$ docker run debian echo "Hello world"
```

- docker run : 컨테이너 시작
- debian : 사용하고자 하는 이미지 이름



```bash
$ docker run -i -t debian /bin/bash  # 컨테이너 내부 쉘(shell) 실행
$ eixt  # 종료
```

- -i , -t : 컨테이너와 tty모드와 대화형 세션 사용하겠다는 의미
- /bin/bash : bash shell 반환

- 컨테이너는 메인 프로세스가 실행되는 동안에만 동작한다





### 4. 기본 명령어

- 도커 실행

```bash
$ docker run -h CONTAINER -i -t debian /bin/bash
```



- 컨테이너 관리

```bash
$ docker ps   # 현재 실행되고 있는 컨테이너들의 상세 정보 반환

$ docker rm [컨테이너 이름]  # 컨테이너 지우기
$ docker rm -v $(docker ps -ap -f status=exited)  # 중지된 모든 컨테이너 ID 반환

$ docker attach [options] [컨테이너 이름] # 컨테이너 내의 메인 프로세서를 볼 수 있게 해줌
$ docker exec  # 컨테이너 내부에 있는 명령 실행
$ docker create  # 이미지를 이용해 컨테이너 생성, 시작은 하지 않음
$ docker kill  # 컨테이너 즉시 종료
$ docker pause  # 컨테이너 내부의 모든 프로세스들을 일시 중지
$ docker unpause 
$ docker restart
...

```



- 도커 정보

```bash
$ docker info
$ docker help
$ docker version
```



- 컨테이너 정보

```bash
$ docker diff [컨테이너 이름]   # 컨테이너가 시작된 이후 변경된 파일들의 목록 출력
$ docker logs [컨테이너 이름]   # 컨테이너 내부에서 발생된 모든 작업 출력

$ docker inspect [컨테이너 이름]  # 정보 출력
$ docker inspect [컨테이너 이름] | grep [정보]  # grep으로 필터링 가능

$ docker port # 컨테이너의 포트 매핑 목록 반환
$ docker top  # 컨테이너 내에서 실행중인 프로세스들의 정보 반환
```



- 이미지 관리

```bash
$ docker build   # 도커파일로 이미지 만들기
$ docker commit [컨테이너 이름] [이미지 저장소/이미지 이름]  # 컨테이너로부터 이미지로 만들기
$ docker history  # 이미지 각 계층에 대한 정보 반환
$ docker image  # 이미지정보 반환
$ docker rmi # 이미지 삭제
$ docker tag  # 이미지에 저장소와 태그이름 지정

$ docker import
$ docker export

```



- 레지스트리 이용

```bash
$ docker login
$ docker logout

$ docker pull
$ docker push
$ docker search
```





### 4. 도커 아키텍처

- 도커 데몬 : 컨테이너 생성,실행 / 모니터링 / 이미지 생성,저장
- 도커 클라이언트 : HTTP를 통해 도커 데몬과 통신
- 도커 레지스트리 : 이미지 저장, 배포