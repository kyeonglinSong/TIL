191009(수)

#하이퍼레저 패브릭 예제 : first-network (byfn)



- byfn : 블록체인 네트워크를 구축하고 스마트 컨트랙트 설치, 호출을 수행하게 되는 예제
- 이번 예제의 네트워크 구성은 두 개의 Org와 각 두 개의 피어(총 4개의 피어),  오더러1, Channel 1인 네트워크이다.



### 0. 하이퍼레저 패브릭 이미지 파일 설치

```bash
$ curl -sSL http://bit.ly/2ysbOFE | bash -s 1.4.0
```

공식 깃허브에서 하이퍼레저 패브릭 샘플 프로젝트와 실행파일들을 내려받는다.

다운로드 받으면 fabric-samples 라는 폴더가 생긴다.





### 1. 네트워크 인증서 생성

‼️ 모든 명령은 기본적으로 fabric-sample 폴더에서 실행한다.



```bash
$ ../fabric-samples/bin/cryptogen generate --config=../fabric-samples/first-network/crypto-config.yaml
```

위 코드를 실행하고 나면 crypto-config라는 폴더가 생성되고, MSP가 생성된다.



- cryptogen은 crypto-config.yaml파일을 이용하여 인증서와 키를 생성하고, 각 조직과 그 구성원에게 MSP를 발급해준다.





### 2. 제네시스 블록 생성

1. 현재 작업 디렉토리 경로를 FABRIC_CFG_PATH라는 변수에 할당

```bash
 $ export FABRIC_CFG_PATH=$PWD
```



2. 제네시스 블록 생성

```bash
$ bin/configtxgen -profile TwoOrgsOrdererGenesis -channelID byfn-sys-channel -outputBlock first-network/channel-artifacts/genesis.block
```

만들어진 제네시스 블록은 first-network/channel-artifacts 에서 확인 가능하다.





###3. 채널 설정 트랜잭션 생성

만들 채널명은 mychannel 이다.

```bash
$export CHANNEL_NAME=mychannel
$bin/configtxgen -profile TwoOrgsChannel -outputCreateChannelTx first-network/channel-artifacts/channel.tx -channelID $CHANNEL_NAME
```

만들어진 channel.tx 파일은 역시 first-network/channel-artifacts 에서 확인 가능하다.





### 4. 각 조직의 앵커 피어 정보 트랜잭션 만들기

- 앵커 피어 : 채널 내의 대표 피어



1. Org1에 속한 앵커 피어 정보 트랜잭션 생성

```bash
$ bin/configtxgen -profile TwoOrgsChannel -outputAnchorPeersUpdate first-network/channel-artifacts/Org1MSPanchors.tx -channelID $CHANNEL_NAME -asOrg Org1MSP
```

first-network/channel-artifacts  안에 Org1MSPanchors.tx 파일이 만들어진 것을 확인할 수 있다.



2. Org2에 속한 앵커 피어 정보 트랜잭션 생성

```bash
$ bin/configtxgen -profile TwoOrgsChannel -outputAnchorPeersUpdate first-network/channel-artifacts/Org2MSPanchors.tx -channelID $CHANNEL_NAME -asOrg Org2MSP
```

마찬가지로 first-network/channel-artifacts  안에 Org2MSPanchors.tx 파일이 만들어진 것을 확인할 수 있다.



여기까지 만든 인증서, 제네시스 블록, 트랜잭션들은 채널을 만드는 데 사용될 것임.





###5. 블록체인 네트워크 동작시키기

```bash
$ docker-compose -f docker-compose-cli.yaml up -d
$ docker ps # 4개의 피어가 구동
```



~~왜 안될까ㅠㅠㅠ 나중에 다시해봐야지...~~