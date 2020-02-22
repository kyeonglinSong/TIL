
# 라이브러리 호출
import crypt # == crypto.js
import merkletools # == merkle
import random
import numpy as np # 문자열과 그 외 기능을 위한 라이브러리
import json # json형식으로 변환하기 위한 라이브러리


# 블록체인을 위해 직접 만들 라이브러리 (후에 번역)
import network as nw 
import utils as ut

mt = merkletools() # default is SHA256

# 블록 구조 클래스
class BlockHeader:
    def __init__(version, index, previousHash, timestamp, merkleRoot, difficulty, nonce):
        self.version = version
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.merkleRoot = merkleRoot
        self.difficulty = difficulty
        self.nonce = nonce


class Block:
    def __init__(header, data):
        self.header = header
        self.data = data


blockchain = [getGenesisBlock()]

def getBlockchain():
    return blockchain

def getLatestBlock():
    return blockchain[len(blockchain)-1]

def getGenesisBlock():
    version = "1.0.0"
    index = 0
    previousHash = np.repeat('0', 2)
    timestamp = 1231006505
    difficulty = 0
    nonce = 0
    data = ["The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"]

    merkleTree = mt.make_tree()
    mt.add_leaf(data)
    merkleRoot = mt.get_merkle_root() or np.repeat('0', 2))
    
    header = BlockHeader(version, index, previousHash, timestamp, merkleRoot, difficulty, nonce)
   
    return Block(header, data)

def generateNextBlock(blockData):
    previousBlock = getLatestBlock()
    currentVersion = ut.getCurrentVersion()
    nextIndex = previousBlock.header.index + 1
    previousHash = calculateHashForBlock(previousBlock)
    nextTimestamp = ut.getCurrentTimestamp()
    difficulty = getDifficulty(getBlockchain())

    #merkletools 라이브러리를 이용하여 머클트리 만들고 머클루트 계산
    merkleTree = mt.make_tree()
    mt.add_leaf(blockData)
    merkleRoot = mt.get_merkle_root() or np.repeat('0', 64))
        
    newBlockHeader = findBlock(currentVersion, nextIndex, previousHash, nextTimestamp, merkleRoot, difficulty)

    return Block(newBlockHeader, blockData)

# 블록체인에 새 블록을 추가하는 함수
def addBlock(newBlock):
    if isValidNewBlock(newBlock, getLatestBlock()): # 유효성 검증 먼저!
        blockchain.append(newBlock) # python list의 append 함수
        return True
    return False

# 블록 채굴 함수
def mineBlock(blockData):
    newBlock = generateNextBlock(blockData)

    if addBlock(newBlock) is True: # 유효한 블록을 추가했다면
        nw.broadcast(nw.responseLatestMsg()) # 네트워크에 블록 전파
        return newBlock
    else:
        return None # 체인에 추가가 되지 않은 경우

# 논스 값 찾는 함수
def findBlock(currentVersion, nextIndex, previoushash, nextTimestamp, merkleRoot, difficulty):
    nonce = 0
    while(True):
        hash = calculateHash(currentVersion, nextIndex, previoushash, nextTimestamp, merkleRoot, difficulty, nonce)
        if hashMatchesDifficulty(hash, difficulty):
            return BlockHeader(currentVersion, nextIndex, previoushash, nextTimestamp, merkleRoot, difficulty, nonce)
        nonce += 1 

# 해시와 관련된 함수들 
# 문제 해결 검사 코드
def hashMatchesDifficulty(hash, difficulty):
    hashBinary = ut.hexToBinary(hash)
    requirePrefix = np.repeat('0', difficulty)

    return hashBinary.startWith(requirePrefix) 

# 해시 계산 함수
def calculateHash(version, index, previousHash, timestamp, merkleRoot, difficulty, nonce):
    return str(crypt.METHOD_SHA256(version + index + previousHash + timestamp 
    + merkleRoot + difficulty + nonce)).upper()


# 블록을 인자로 하는 블록 해시 계산 함수
def calculateHashForBlock(block):
    return claculateHash( # 해시계산 함수로 계산한 값을 반환
        block.header.version,
        block.header.index,
        block.header.previousHash,
        block.header.timestamp,
        block.header.merkleRoot,
        block.header.difficulty,
        block.header.nonce
    )

# 블록 생성 간격 조정을 위한 상수(파이썬엔 상수 없음) 역할을 하는 안바뀔 변수들.
BLOCK_GENERATION_INTERVAL = 10 # in seconds
DIFFICULTY_ADJUSTMENT_INTERVAL = 10 # in secnds

# 현재 난이도 반환 함수
def getDifficulty(aBlockchain):
    latestBlock = aBlockchain[len(aBlockchain)-1]

    if ((latestBlock.header.index % DIFFICULTY_ADJUSTMENT_INTERVAL == 0) and (latestBlock.header.index != 0)) is True:
        return getAdjustedDifficulty(latestBlock, aBlockchain)
    
    return latestBlock.header.difficulty

# 조정된 난이도 반환 함수
def getAdjustedDifficulty(latestBlock, aBlockchain):
    prevAdjustmentBlock = aBlockchain[len(aBlockchain)-DIFFICULTY_ADJUSTMENT_INTERVAL]
    timeTaken = latestBlock.header.timestamp - prevAdjustmentBlock.header.timestamp
    timeExpected = BLOCK_GENERATION_INTERVAL * DIFFICULTY_ADJUSTMENT_INTERVAL

    if timeTaken < (timeExpected * 2):
        return prevAdjustmentBlock.header.difficulty + 1
    elif timeTaken > (timeExpected*2):
        return prevAdjustmentBlock.header.difficulty - 1
    else:
        return prevAdjustmentBlock.header.difficulty



# 블록체인 검증 함수들
# 유효한 블록구조인지 검증하는 함수
def isValidBlockStructure(block): 
    return type(block.header.version) is str
        and type(block.header.index) is int
        and type(block.header.previousHash) is str
        and type(block.header.timestamp) is int
        and type(block.header.merkleRoot) is str
        and type(block.header.difficulty) is int
        and type(block.header.nonce) is int
        and type(block.data) is list # list가 맞는지 모르겠음!


# 유효한 타임스탬프인지 검증하는 함수
def isValidTimestamp(newBlock, previousBlock):
    return (previousBlock.header.timestamp-60 < newBlock.header.timestamp) and newBlock.header.timestamp-60 < ut.getCurrentTimestamp()

# 새로운 블럭이 유효한 블럭인지 검사하는 함수
def isValidNewBlock(newBlock, previousBlock):
    if isValidBlockStructure(newBlock) is False:
        print('invalid block structure: ' + json.dumps(newBlock)) # 여기 바꿔야함
        return False
    elif previousBlock.header.index+1 != newBlock.header.index:
        print("invalid previousHash")
        return False
    elif  (newBlock.data.length != 0 and (merkle("sha256").sync(newBlock.data).root() != newBlock.header.merkleRoot)) or (len(newBlock.data) == 0 and (np.repeat('0', 64)) != newBlock.header.merkleRoot))
        print('invalid merkleRoot')
        return False
    elif isValidTimeStamp(newBlock, previousBlock) is False:
        print('invalid timestamp')
        return False
    elif hashMatchesDifficulty(calculateHashForBlock(newBlock), newBlock.header.difficulty) is False:
        print('invalid hash : '+ calculateHashForBlock(bewBlock))
        return False
    return True

# 체인 유효성 검증 함수
def isValidChain(blockchainToValidate):
    if json.dumps(blockchainToValidate[0]) != json.dumps(genesisBlock()): #json 라이브러리의 dumps 함수 사용해서 json형식으로 바꿔줌. 
        return False
    tempBlocks = [blockchainToValidate[0]]
    for i in range(len(blockchain)):
        if isValidNewBlock(blockchainToValidate[i], tempBlocks[i-1]) is True:
            return tempBlocks.append(blockchainToValidate[i])
        else:
            return False
    return True

# newBlock의 길이가 원래 블록 길이보다 길 경우, 긴 블록이 맞다는 규칙에 의해서 블록 대체
def replaceChain(newBlocks):
    if (isValidChain(newBlocks) is True) and (len(newBlocks)>len(blockchain) or (len(newBlocks)==len(blockchain) and random.boolean())):
        print("Received blockchain is valid. Replacing current blockchain with received blockchain")
        nw.broadcast(nw.responseLatestMsg())
    else:
        print("Received blockchain invalid")