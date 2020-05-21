# [자료구조/알고리즘] 삽입정렬(insertion sort)



### * 시간복잡도 : O(n) ~ O(n^2)



### 방법

1. 맨 앞이 아닌 수 하나 선택
2. 앞으로 계속 탐색. 이때 위치를 하나씩 밀어간다. (j를 계속 비워간다고 생각하면 됨!)
   * arr[j+1] = arr[j]
3. 적절한 위치에 도달하면 수를 삽입
4. 반복!



### 코드 (C++)

```c++
#include <iostream>
using namespace std;

void insertion_sort(int arr[])
{
    int j, next;
    for(int i=1 ; i<10 ; i++)
    {
        next = arr[i];
        for(j=i-1 ; j>=0 && next<arr[j] ; j--)
            arr[j+1] = arr[j];
        arr[j+1] = next;

        for(int i=0 ; i<10 ; i++)
            cout << arr[i] << " ";
        cout << "\n";
    }

    cout << "\nresult : ";
    for(int i=0 ; i<10 ; i++)
        cout << arr[i] << " ";
}


int main()
{
    int arr[10] = {2,6,8,4,3,1,10,9,5,7};
    insertion_sort(arr);

    return 0;
}
```

