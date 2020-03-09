200309(월)

# [java] List, ArrayList, LinkedList



###1. List와 ArrayList의 차이

- List list = new ArrayList()
- ArrayList list = new ArrayList()



List는 인터페이스이고 arrayList는 List에 상속된 클래스이다.

따라서 ArrayList는 단독으로 사용할 수 없고, List를 상속받아 사용해야 한다.



### 2. ArrayList vs LinkedList

+ ArrayList : 검색이 빠름 / 삽입삭제 느림
+ LinkedList : 검색이 느림 / 삽입삭제 빠름