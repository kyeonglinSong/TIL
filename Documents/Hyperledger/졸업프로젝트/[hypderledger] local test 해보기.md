 

200221(금)

# [Hyperledger] local test 실습

IBM Blockchain Lab 6: Smart Contract Development

### 1. Preface

- set of tools for building, operation, growing blockchain network
- hyperledger fabric v1.4
- sample 스마트 컨트랙트 사용하여 contracts import 하는 법, 클라이언트 애플리케이션을 통해 개발환경과 interact 하는법을 배움 (fabcar 예제)

### 2. Overview of the lab environment and scenario

#### 2-1. Lab scenario

- 이 실습을 하고나면 클라이언트 애플리케이션을 통해 contract의 transcstions을 invoke 할 수 있음.

### 3. Using an Existing Contract

- FabCar 에는 5개의 transactions 이 있음.
  - initLedger
    - `ctx.stub.putState()`
    - `putState()` : context parameter인 `ctx`를 통해 트랜잭션에 접근가능하게 만든다.
    - `ctx` : 언제나 transaction의 첫번째 파라미터이다.
- IBP 사용법 - Local test

1. Smart Contracts의 More action에서 Package Open Project -> package 이름 입력 -> 버전 입력
   - 이제 패키지를 blockchain peer에 install하면 됨.
2. Local Fabric development environment 만들기
   - Fabric Environments에서 Clik to start -> SUCCESS 뜨면 만들어진것임.
   - 그 후 Fabric Environment를 보면 smart contract, channels, nodes, organizations등이 생겨있다.
3. Smart Contracts -> Install -> fabcar@1.0.0 선택으로 피어에 체인코드를 install
4. Instantiate -> fabcar@1.0.0 -> Optional : initLedger 입력 -> no argument -> default 설정 선택
   - 컨트랙트 루트 디렉토리에 **package.json** 파일이 꼭 필요하구나...
   - 이제 gateway를 통해 network에 연결할 수 있다! 트랜잭션 날릴 수 있다!
5. Fabric Gateway -> Local Fabric