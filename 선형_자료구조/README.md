# 배열/리스트

## 리스트

### enumerate 

```python
for idx, stuent in enumerate(students):
  print(idx, student) 
```

### zip 

```python
courses = ["math", "history", "korean"]
scores = [100, 10, 60, 40]
kor_courses = ["수학", "역사", "국어"]

for course, score, kor_course in zip(courses, scores, kor_courses):
  print(course, score, kor_course)   
```

### comprehension 

[(변수를 활용한 계산식) for (변수) in ( iterable )]
```python
arr = [i * 2 for i in range(10)]
print(arr) # [0,2,4,6,8,10,12,14,16,18]
```

응용

```python
arr = [n for n in range(10) if n%2 ==0]
print(arr) #[0,2,4,6,8]
```

```python
matrix = [[1,2,3], [4, 5] [6, 7, 8, 9]]
flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix) # [1.2.3.4.5.6.7.8.9]
```

중첩된 리스트 

```python
arr = [[n for n in range(m + 1)] for m in range(3)]
print(arr) # [[0], [0,1], [0,1,2]]
```

딕셔너리 컴프리헨션 

```python
students = ["james", "cameroon", "mellon", "indo", "buzzi"]
class_info = {idx: student for idx, student in enumerate(students)}
class_info # {0: "james", 1: "cameroon", 2: "mellon", 3:"indo", 4:"buzzi" }
```

컴프리헨션을 입력받는 함수
#### sum : 입력받은 값의 합계를 구합니다. 

```python
sum(num for num in range(1,4)) # 6
```

#### max: 입력받은 값의 최댓값을 구합니다.

```python
max(num for num in range(1,4)) #3
```

#### min: 입력받은 값의 최솟값을 구합니다. 
```python
min(num for num in range(1,4)) #1
```

#### all: 모든 값이 True라면 결과로 True가 나오고, 하나라도 False가 있다면 결과는 False입니다. 
```python
all(num < 4 for num in range(1,4)) # True
all(num % 2 == 0 for num in range(1,4)) # False
```

#### any: 어느 하나라도 True가 존재한다면 결과를 True 이고, 아니면 False입니다. 
```python
any(num % 2 == 0 for num in range(1,4)) #True
any(num == 4 for num in range(1,4)) #False
```

#### sorted: 입력받은 값들을 오름차순으로 정렬합니다. 
```python
nums = [4, 3, 2]
sorted(num for num in nums) # [2,3,4]
```
## 딕셔너리[해시맵]

### dictionary 
파이썬에서의 해시 함수는 딕셔너리로 구현되어 있습니다. 
```python
dictionary = {"key": "value"}
```

### defaultdict
딕셔너리는 존재하지 않는 키를 참조하려고 하면 에러가 발생하기 때문에, 키를 참조하기 전에 키가 존재하는지를 미리 확인해야만 함. 

```python
from collections import defaultdict
temp = {"this": "yes"}
if "this" in temp:
  print(temp["this"])
```

defaultdict는 타입을 입력으로 받고 해당 타입의 기본값을 존재하지 않는 키의 기본값으로 사용합니다. 예를 들어, int의 경우는 기본값이 0. 

```python
int_dict = defaultdict(int)
int_dict["a"] += 1
int_dict("b"]
print(int_dict)
```

list 타입의 경우는 비어 있는 리스트를 기본값으로 사용. 
```python
list_dict = defaultdict(list)
list_dict["a"].append(1)
list_dict("b"]
print(int_dict)
```
dict 타입은 비어 있는 딕셔너리를 기본값으로 사용. 
```python
dict_dict = defaultdict(dict)
dict_dict["a"]["b"] = 1
dict_dict("c"]
print(dict_dict)
```
## Counter
Counter는 딕셔너리처럼 키와 밸류로 구성된 자료형으로, 딕셔너리와 거의 동일하게 사용할 수 있음. Counter를 사용하면 원소별로 등장 횟수를 쉽게 셀 수 있음. 
```python
fruits = ["orange" , "pear", "apple", "apple", "apple", "pear"]
```

```python
from collections import Counter
  count = Counter(fruits)
  print(count)
```

count를 빈도순으로 내림차순 정렬한 리스트 frequency 를 만들 때. 여기서는 reverse = True 를 써도 되지만 다음과 같이 더 간결하게 작성할 수 있음.
```python
frequency = sorted(count.items(), key = lambda x: -x[1])
print(frequency)
# [("apple", 3), ("pear", 2), ("orange",1)]
```
만일 Counter를 쓴다면, 아래와 같이 할 수 있음.
```python
count = Counter(fruits)
count.most_common()
# [("apple", 3), ("pear", 2), ("orange",1)]
```

## 셋[집합]
셋은 주로 중복값을 제거하거나, 중복이 허용되지 않는 값의 목록을 만을 때 사용함. 

### 셋의 연산 
```python
nums1 = {1,2,3}
nums2 = {2,3,4}
```
#### 교집합
```python
nums1 & nums2 # {2, 3}
```
#### 차집합 
```python
nums1 - nums2 # {1}
nums2 - nums1 # {4}
```
#### 합집합
```python
nums1 | nums2 # {1,2,3,4}
```

## 스택 
### pop/push
```python
stack = []
stack.append(1)
stack.append(2)
stack.pop()
print(stack) # [1]
```
## 큐와 데크

### pop/push 
```python
queue = []
queue.append(1)
queue.append(2)
queue.pop(0)
print(queue) # [2]
```
### 데크(dequeue)
스택과 큐의 특징을 모두 가지고 있는 자료구조. 즉 Pop 과 push를 자료형의 앞과 뒤에서 모두 할 수 있음. 
```python
dequeue = []
dequeue.append(1)
dequeue.appned(2)
dequeue.pop(0)
dequeue.append(3)
dequeue.pop()
print(dequeue) # [2] 
```
```python
from collections improt deque
dq = deque([1,2,3,4,5])
print(dq) #deque([1,2,3,4,5])
print(dq.pop()) # 5
print(dq.popleft()) # 1
```

### 프로그래머스 문제 
[옹알이(1)](https://school.programmers.co.kr/learn/courses/30/lessons/120956) </br>
[문자열 계산하기](https://school.programmers.co.kr/learn/courses/30/lessons/120902) </br>
[OX퀴즈](https://school.programmers.co.kr/learn/courses/30/lessons/120907) </br>
[숨어있는 숮자의 덧셈](https://school.programmers.co.kr/learn/courses/30/lessons/120864) </br>
[인덱스 바꾸기](https://school.programmers.co.kr/learn/courses/30/lessons/120895) </br>
[문자열 밀기](https://school.programmers.co.kr/learn/courses/30/lessons/120921) </br>
[문자열 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/140108) </br>
[옹알이(2)](https://school.programmers.co.kr/learn/courses/30/lessons/133499) </br>

# 구현
### 프로그래머스 문제
[가위 바위 보](https://school.programmers.co.kr/learn/courses/30/lessons/120839) </br>
[연속된 수의 합](https://school.programmers.co.kr/learn/courses/30/lessons/120923) </br>
[치킨 쿠폰](https://school.programmers.co.kr/learn/courses/30/lessons/120884) </br>
[k의 개수](https://school.programmers.co.kr/learn/courses/30/lessons/120887) </br>
[369게임](https://school.programmers.co.kr/learn/courses/30/lessons/120891) </br>
[카드 뭉치](https://school.programmers.co.kr/learn/courses/30/lessons/159994) </br>
[로또의 최고 순위와 최저 순위](https://school.programmers.co.kr/learn/courses/30/lessons/77484) </br>

### 프로그래머스 문제
(잘라서 배열로 저장하기) [https://school.programmers.co.kr/learn/courses/30/lessons/120913]
(2차원으로 만들기) [https://school.programmers.co.kr/learn/courses/30/lessons/120842]
(7의 개수) [https://school.programmers.co.kr/learn/courses/30/lessons/120912]
(가장 큰 수 찾기) [https://school.programmers.co.kr/learn/courses/30/lessons/120899]
(모의고사) [https://school.programmers.co.kr/learn/courses/30/lessons/42840]
(행렬의 덧셈 1) [https://school.programmers.co.kr/learn/courses/30/lessons/12950]
(바탕화면 정리1) [https://school.programmers.co.kr/learn/courses/30/lessons/161990]

(로그인 성공?) [https://school.programmers.co.kr/learn/courses/30/lessons/120883]
(성격 유형 검사하기) [https://school.programmers.co.kr/learn/courses/30/lessons/118666] 
(가장 가까운 같은 글자) [https://school.programmers.co.kr/learn/courses/30/lessons/142086]
(숫자 문자열과 영단어) [https://school.programmers.co.kr/learn/courses/30/lessons/81301]
(완주하지 못한 선수) [https://school.programmers.co.kr/learn/courses/30/lessons/42576]
(전화번호 목록) [https://school.programmers.co.kr/learn/courses/30/lessons/42577]
(의상) [https://school.programmers.co.kr/learn/courses/30/lessons/42578]
(베스트앨범) [https://school.programmers.co.kr/learn/courses/30/lessons/42579]

(외계어 사전) [https://school.programmers.co.kr/learn/courses/30/lessons/120869]
(중복된 문자 제거) [https://school.programmers.co.kr/learn/courses/30/lessons/120888]
(최빈값 구하기) [https://school.programmers.co.kr/learn/courses/30/lessons/120812]
(폰켓몬) [https://school.programmers.co.kr/learn/courses/30/lessons/1845]
(둘만의 암호) [https://school.programmers.co.kr/learn/courses/30/lessons/155652]
(신고 결과 받기) [https://school.programmers.co.kr/learn/courses/30/lessons/92334]
(컨트롤 제트) [https://school.programmers.co.kr/learn/courses/30/lessons/120853]
(같은 숫자는 싫어) [https://school.programmers.co.kr/learn/courses/30/lessons/12906]
(햄버거 만들기) [https://school.programmers.co.kr/learn/courses/30/lessons/133502]
(올바른 괄호) [https://school.programmers.co.kr/learn/courses/30/lessons/12909]
(배열 회전시키기) [https://school.programmers.co.kr/learn/courses/30/lessons/120844]
(기능개발) [https://school.programmers.co.kr/learn/courses/30/lessons/42586]
(프로세스) [https://school.programmers.co.kr/learn/courses/30/lessons/42587]
