# [자료구조, 알고리즘] 버블정렬(bubble sort)



### 시간복잡도 : O(N^2)

시간이 오래걸리나 코드가 단순해서 입력크기가 작다면 쓰기 좋다.



### 방법 (오름차순 정렬 기준)

1. 전체 반복은 n만큼
2. 안쪽 반복문은 n-1만큼
3. 안쪽 반복문에서 오른쪽 옆 수와 자신을 비교, 자신이 더 크면 둘을 교체한다.
4. 안쪽 반복문 한번이 끝나면 그중 제일 큰 수가 맨 뒤로 가 있는다.
5. 맨 뒷수를 제외하고 다시 반복.



### 코드(C++)

```C++
#include <iostream>
using namespace std;

int arr[101];

void bubble(int n)
{
    for(int i=0 ; i<n-1 ; i++)
    {
        for(int j=0 ; j<n-i ; j++)
        {
            if(arr[j-1] > arr[j])
            {
                int temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;
            }    
        }
    }
    for(int i=0 ; i<n ; i++)
        cout << arr[i] << " ";
}

int main()
{
    int n;
    cin >> n;

    for(int i=0 ; i<n ; i++)
        cin >> arr[i];
  
    bubble(n);

    return 0;
}
```



