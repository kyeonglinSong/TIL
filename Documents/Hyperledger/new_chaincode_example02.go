// makeIdAndVal : 계정 생성(ID)과 해당 계정에 토큰(Val) 발행
// moveVal : a 계정에서 b 계정으로 토큰 거래
// queryById : 각 계정별 잔액(balance) 조회
// query : 전체 조회

package main

import {
	"fmt"
}
// fmt : 표준 입출력 패키지

// ValInfo 구조체 : 생성한 계정과 토큰을 담는다.
type ValInfo struct{
	Id string 'json: "id"'
	Val int 'json: "val, string"'
}


// Init 함수 : 토큰 발행과 동시에 초기값을 지정함
fucn (t *SimpleChaincode) Init(stub shim.ChaincodeStubInterface) pd.Response { // pd 변수 : 피어의 정보를 담는 버퍼로 사용
	fmt.Println("Chaincode Practice Init")
	return shim.Success(nil)  // shim : 트랜잭션을 발생시키는 하이퍼레저의 패키지
}


// Invoke 함수 : 사용자가 호출하는 함수를 분기함.
func (t *SimpleChaincode) Invoke(stub shim.ChaincodeStubInterface) pd.Response {
	fmt.Println("ex02 Invoke")

	function, args := stub.GetFunctionAndParameters()  // stub 인터페이스의 GetFunctionAndParameters 함수를 통해 사용자로부터 function과  args를 받아옴.
	
	// 위에서 받은 function 값으로 함수르 분기
	// 받은 값이 3개 이상일 때, 맨 앞 값은 function, 그 뒤의 값들은  args 값으로 전달된다.
	if function == "makeIdAndVal"{
		return t.invoke(stub, args)  // invoke 하면 트랜잭션 발생

	} else if function == "query" { 
		return t.query(stub, args)

	} else if function == "moveVal" {
		return t.moveVal(stub, args)

	} else if function == "queryById" {
		return t.queryById(stub, args)

	}

	return shim.Error("Invalid invoke function name!")
}
