# [자료구조/알고리즘] 선택정렬(selection sort)



### 시간복잡도 : O(logN)



### 방법 (오름차순 정렬 기준)

1. 첫 인덱스는 0(혹은1)이다.
2. 전체를 탐색하며 가장 작은 수를 선택한다.
3. 수를 인덱스 위치에 놓는다.
4. 인덱스를 하나 늘리고 다시 탐색한다.
5. 배열 크기 -1 만큼 탐색한다.



### 코드(C++)

```C++
#include <iostream>
using namespace std;

void selection_sort(int arr[])
{
    for(int i=0 ; i<10-1 ; i++)
    {
        int num = 10000000;
        int index;
        for(int j=i ; j<10 ; j++)
        {
            if(num>arr[j])
            {
                num = arr[j];
                index = j;
            }
        }
        int temp = arr[index];
        arr[index] = arr[i];
        arr[i] = temp;

        for(int j=0 ; j<10 ; j++)
            cout << arr[j] << " ";
        cout <<"\n";
    }

    cout <<"결과 : ";
    for(int j=0 ; j<10 ; j++)
        cout << arr[j] << " ";
}

int main()
{
    int arr[10] = {2,6,7,8,3,1,10,9,5,4};
    selection_sort(arr);

    return 0;
}
```



