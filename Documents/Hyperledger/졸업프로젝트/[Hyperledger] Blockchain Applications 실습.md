200223(일)

# [Hyperledger] Blockchain Applications 실습

IBM Blockchain Lab 7: Blockchain Application



- **prefer** : 샘플 애플리케이션을 가지고 어떻게 블록체인과 interaction하는 애플리케이션을 개발, run하는지 배울거임.



- ./start.sh (./network-start.sh)

  베이직 nw를 구성하는 도커 컨테이너를 시작한다.

  **fabric-peer**, **fabric-ca**, **fabric-couchdb** and **fabric-orderer** components 가 실행되어야함.

  ![image-20200224005115380](/Users/blossommilktea/Library/Application Support/typora-user-images/image-20200224005115380.png)

- **working as MagnetoCorp.**

  magnetocorp의 cli로 이동 -> ./monitordocker.sh net_basic 으로 도커 모니터링 실행



- magnetocorp가 commercial paper를 issue 해야함.

  -> 따라서 peer에  체인코드를 install하고 instantiate 해야함.

  -> **fabric-tools **라는 도커 이미지를 사용할것임. cli에서 다음 명령어 입력

  `docker-compose -f docker-compose.yml up -d cliMagnetoCorp`