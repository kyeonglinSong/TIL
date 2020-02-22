#Tutorial 1. Local smart contract development



###1. Create a new smart contract project

- 프로젝트 폴더, 프로젝트 골격 생성!



###2. Understand the smart contract

- @Transaction() : 렛저 내용을 바꿀 수 있음. submitted transaction type

  myAsetId : key

  value : value

- @Transaction(false) : 렛저 내용을 변경하지 않음.  evaluated transaction type



### 3. Package the smart contract

드디어 스마트 컨트랙트를 만든다!

스마트 컨트랙트 프로젝트는 **.CDS** 파일로 패키징된다. **.CDS** 파일은 하이퍼레저 패브릭 피어를 설치할 수 있는 파일 타입이다.



- smart contract panel, ...클릭, package open project 선택
- demoContract@0.0.1 이 생성됨



방금 생성 한 패키지는 모든 Hyperledger Fabric 피어에 설치 될 수 있습니다 (올바른 버전으로 실행). 예를 들어, 마우스 오른쪽 단추를 클릭하고 "내보내기 패키지"를 선택한 다음 IBM Blockchain Platform 운영 도구 콘솔을 사용하여 클라우드 환경에 배치 할 수 있습니다. 나중에이 작업을 수행하는 방법을 배웁니다. 지금은 VS 코드 확장으로 사전 구성된 런타임에 패키지를 로컬로 배포하므로 아직 패키지를 내보낼 필요가 없습니다!





### 4. Fabric Environments

- Local Fabric  ○ (click to start).

얘 누르면 도커 실행해준다. 완료되면 fabric environments에 smart contracts / Channels / Nodes / Organizations 가 생성된다. 

- Smart contracts
- Channels
- Nodes : peer를 포함함. 피어 명명은 Hyperledger Fabric 규칙을 따른다.
- Organizations 





### 5. Install the smart contract

실제 네트워크에서 transcatino을 endorsing할 각 org은 스마트 컨트랙트를 install 한 다음, channel에서 instantiate한다.



여기서는 single peer에 코드를 install 한 후 mychannel에 instantiate 한다.

- Fabric environments 패널에 + install 누름
- 설치할 코드를 선택





### 6. Instantiate the smart contract

install 까지 한 코드는 아직 클라이언트 애플리케이션에서 호출할 준비가 되지 않았음! nw의 모든 조직이 사용할 수 있게 instantiate 해야한다.

여러 조직이 참여하는 경우, 채널에서 instantiate 하기 전에 피어마다 스마트 컨트랙트를 install 해야함.

- +instantiate 누름
- 설치할 코드 선택





### 7. Submit and evaluate transactions

fabric gateway는 클라이언트 애플리케이션과 피어의 연결이다. 런타임을 시작하면 자동으로 생성된다! 게이트웨이를 사용하려면 해당 nw에서 트랙잭션에 유효한 ID가 필요하다.

- fabric gateway의 local fabric 클릭
- 



