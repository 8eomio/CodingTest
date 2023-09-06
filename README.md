# python_coding_test

### 시간복잡도 확인하기

문제에서 가장 먼저 확인해야 하는 내용은 시간제한(수행시간 요구사항)이다.

시간제한이 1초인 문제를 만났을때, 일반적인 기준은 다음과 같다.

- N의 범위가 500인 경우 : 시간 복잡도가 O(N3)인 알고리즘을 설계
- N의 범위가 2,000인 경우 : 시간 복잡도가 O(N2)인 알고리즘을 설계
- N의 범위가 100,000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계
- N의 범위가 10,000,000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계

많은 문제를 풀면서 감을 익히는게 좋다.

**일반적인 알고리즘 문제 해결 과정은 다음과 같다.**

1. 지문 읽기 및 컴퓨터적 사고
2. 요구사항(복잡도) 분석
3. 문제 해결을 위한 아이디어 찾기
4. 소스코드 설계 및 코딩

일반적으로 출제자들은 핵심 아이디어를 캐치한다면 간결하게 소스코드를 작성할 수 있는 형태로 제출한다.

### 리스트 컴프리헨션

- 0부터 9까지의 수를 포함하는 리스트

```python
array = [i for i in range(10)]
print(array) 

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

- 조건문

```python
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1,10)]
```

- **2차원 리스트 초기화**

리스트 컴프리헨션은 N X M 크기의 2차원 리스트 초기화할 때 매우 유용하다.

```python
# N X M 크기의 2차원 리스트 초기화
array = [[0] * m for _ in range(n)]
```

## 리스트 관련 기타 메서드

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/47eeb7ff-6e88-4e79-bf67-d6879b6b0ddc/_2021-01-12__8.55.21.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/47eeb7ff-6e88-4e79-bf67-d6879b6b0ddc/_2021-01-12__8.55.21.png)

### 리스트에서 특정 값을 가지는 원소를 모두 제거하기

```python
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} # 집합 자료형

# remove_list에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result) // [1, 2, 4]
```

## 문자열

- 문자열에 대해서도 마찬가지로 인덱싱과 슬라이싱을 이용할 수 있다.
    - 다만 문자열은 특정 인덱스의 값을 변경할 수는 없다.(Immutable)

## 튜플

### 튜플을 사용하면 좋은 경우

- 서로 다른 성질의 데이터를 묶어서 관리해야 할 때
    - 최단 경로 알고리즘에서는 (비용, 노드 번호)의 형태로 튜플 자료형을 주로 사용한다.
- 데이터의 나열을 해싱(Hashing)의 키 값으로 사용해야 할 때
    - 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될 수 있다.
- 리스트보다 메모리를 효율적으로 사용해야 할 때

## 사전 자료형

- 키(Key)와 값(Value)의 쌍을 데이터로 가지는 자료형이다.
    - 앞서 다루었던 리스트나 튜플이 값을 순차적으로 저장하는 것과는 대비된다.
- 사전 자료형은 키와 값의 쌍을 데이터로 가지며, 원하는 '변경 불가능한(Immutable) 자료형'을 키로 사용할 수 있다.
- 파이썬의 사전 자료형은 해시 테이블(Hash Table)을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.
- 다른 프로그래밍 언어에서의 해시 테이블 역할을 수행한다.

```python
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data) 
# {'사과' : 'Apple', '바나나' : 'Banana', '코코넛' : 'Coconut'}

if '사과' in data:
	print("사과있다") # 사과있다
```

### 사전 자료형 관련 메서드

- 사전 자료형에서는 키와 값을 별도로 뽑아내기 위한 메서드를 지원한다.
    - 키 데이터만 뽑아서 리스트로 이용할 때는 keys()함수를 이용한다.
    - 값 데이터만을 뽑아서 리스트로 이용할 때는 values()함수를 이용한다.

```python
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()

print(key_list)       # dict_keys(['사과', '바나나', '코코넛'])
print(values_list)    # dict_values(['Apple', 'Banana', 'Coconut'])

# 리스트로 형 변환을 해주는 것이 사용하기 좋다.
print(list(key_list)) # ['사과', '바나나', '코코넛']

for key in key_list:
	print(data[key])

# Apple
# Banana
# Coconut
```

## 집합 자료형

- 집합은 중복을 허용하지 않으며, 순서가 없다는 특징을 갖는다.
- 집합은 set()함수 혹은 중괄호를 사용하여 초기화 할 수 있다.
- 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.

```python
data = set([1, 1, 2, 3, 4, 4, 5])
print(data) # {1, 2, 3, 4, 5}

data = {1, 1, 2, 3, 4, 4, 5}
print(data) # {1, 2, 3, 4, 5}
```

### 집합 자료형의 연산

기본적인 집합 연산으로는 합집합, 교집합, 차집합 연산 등이 있다.

```python
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 합집합
print(a | b) # {1, 2, 3, 4, 5, 6, 7}

# 교집합
print(a & b) # {3, 4, 5}

# 차집합
print(a - b) # {1, 2}
```

### 집합 자료형 관련 함수

```python
data = set([1, 2, 3])
print(data) # {1, 2, 3}

# 새로운 원소 추가
data.add(4)
print(data) # {1, 2, 3, 4}

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data) # {1, 2, 3, 4, 5, 6}

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data) # {1, 2, 4, 5, 6}
```

### 사전 자료형과 집합 자료형의 특징

- 리스트나 튜플은 순서가 있기 때문에 인덳이을 통해 자료형의 값을 얻을 수 있다.
- 사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.
    - 사전의 키 혹은 집합의 원소를 이용해 O(1)의 시간복잡도로 조회한다.

### 조건문의 간소화

- 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현할 수 있다.

```python
score = 85
result = "Success" if score >= 80 else "Fail"

print(result) # Success
```

## 람다 표현식

- 람다 표현식을 이용하면 함수를 간단하게 작성할 수 있다.
    - 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징이다.

```python
def add(a, b):
	return a + b

# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))
```

### 람다 표현식 예시 : 내장 함수에서 자주 사용되는 람다 함수

```python
array = [('홍길동' , 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
	return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))
```

### 람다 표현식 예시: 여러 개의 리스트에 적용

```python
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)

prnit(list(result))
# [7, 9, 11 ,13, 15]
```

map 함수는 각각의 원소에 하나의 함수를 적용하고자 할때 사용한다.

# 입출력

알고리즘 문제는 적절한 입력이 주어졌을 때, 그것을 사용해서 적절한 알고리즘을 수행해 결과를 출력해야 한다.

- 파이썬에서 데이터를 입력받을 때 `input()` 함수를 사용해 한 줄의 문자열을 입력받는다.
- 입력받은 문자열을 정수형 데이터로 처리하기 위해서는 `int()` 함수를 사용한다.

여러 개의 데이터를 입력받을 때에는 데이터가 공백으로 구분되는 경우가 많은데, 이때는 입력받은 문자열을 띄어쓰기로 구분해서 각각 정수 자료형 데이터로 저장하는 코드가 자주 사용된다.

> 이 코드는 정말 자주 사용되므로 외우고 있는 것이 좋다고 한다.

- `list(map(int, input().split()))` 이용

    1. `input()`으로 입력받은 문자열을 `split()`을 이용해 공백으로 나눈 리스트로 변환

    2. `map` 을 이용해서 해당 리스트의 모든 원소에 `int()` 함수 적용

    3. 그 결과를 다시 `list()`로 바꿔서 입력받은 문자열을 띄어쓰기로 구분해서 각각 숫자형으로 저장

만약 입력 하나 하나가 줄바꿈을 통해 따로 입력된다면, `int(input())`을 여러 번 사용해서 받으면 된다.

### 데이터 입력 예시

```python
# 데이터 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분해서 입력
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)

# 입력 : 533 78 90 12 83
# 출력 : [90, 83, 78, 33, 12]
```

### 공백 기준으로 적은 수의 데이터 입력

```python
# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())

print(n, m, k)

# 입력 : 1, 2, 5
# 출력 : 1 2 5
```

### 입력의 개수가 많은 경우

- 입력의 개수가 많은 경우 동작 속도가 느린 `input()` 함수를 사용하면 시간 초과로 오답 판정을 받을 수도 있다
- 이 때에는 파이썬 sys 라이브러리에 정의되어 있는 `sys.stdin.readline()` 함수를 이용한다.
- `readline()` 으로 입력하면 입력 후 엔터 키가 줄 바꿈 기호로 입력되는데, 이 공백 문자를 제거하기 위해 `rstrip()` 함수를 사용해야 한다.

### `readline()` 함수 사용 소스코드 예시

```python
import sys

# 문자열 입력받기
data = sys.stdin.readline().rstrip()
print(data)

# 입력 : "Hello World"
# 출력 : Hello World
```

## 데이터 출력

파이썬에서는 `print()` 함수를 이용해서 데이터를 출력한다.

- `print()` 안에 변수나 상수를 매개 변수로 입력받아 출력한다.
- 각 변수를 콤마(,)로 구분하여 넣을 경우, 각 변수가 띄어쓰기로 구분되어 출력된다.
- `print()`는 기본적으로 출력 이후에 줄 바꿈을 수행하기 때문에, `print()`를 사용할 때마다 줄이 변경된다.

```python
a = 1
b = 2
print(a) # 1
print(b) # 2
print(a, b) # 1 2
```

### 문자열과 수를 함께 출력해야 하는 경우 주의할 점

- 단순히 더하기 연산자(+)를 이용해서 문자열과 수를 더하면 오류가 발생한다.
    - 1. `str()` 함수를 이용해서 변수 데이터를 문자열로 바꿔주거나
    - 2. 각 자료형을 콤마(,)를 기준으로 구분하여 출력하면 된다.
    - 3. Python 3.6 이상부터는 f-string 문법을 이용해 간단히 출력 가능하다
    - f-string을 이용하면 단순히 중괄호({}) 안에 변수를 넣음으로써, 자료형의 변환 없이도 간단히 문자열과 정수를 함께 넣을 수 있다.

### 잘못된 출력 예시

```python
# 출력할 변수
answer = 9

print("정답은 " + answer + "입니다.")

# TypeError: can only concatenate str (not "int") to str
```

### 변수를 문자열로 바꿔 출력하는 소스코드

```python
# 출력할 변수
answer = 9

print("정답은 " + str(answer) + "입니다.")

# 정답은 9입니다.
```

### 콤마로 구분하여 출력하는 소스코드

```python
# 출력할 변수
answer = 9

print("정답은 ", str(answer), "입니다.")

# 정답은 9 입니다.
```

각 변수를 콤마로 구분해서 출력하는 경우, 변수의 값 사이에 의도하지 공백이 삽입될 수 있으니 주의하자!

### f-string 사용 소스코드

```python
# 출력할 변수
answer = 9

print(f"정답은 {answer}입니다.")

# 정답은 9 입니다.
```

# 람다 표현식

파이썬에서 람다 표현식을 사용하면 함수를 한 줄에 작성해 간단하게 사용할 수 있다.

### 예시

```python
def add(a, b):
	return a + b

# 일반적인 add() 메서드 사용
print(add(3, 7)) # 10

# 람다 표현식으로 구현한 add() 메서드
print(lambda a, b: a + b)(3, 7)) # 10
```

# 코딩 테스트 준비 시 반드시 알아두어야 할 파이썬 라이브러리

- 내장 함수: `print()`, `input()`과 같은 기본 입출력 기능부터 `sorted()`와 같은 정렬 기능을 포함하는 내장 라이브러리.
- itertools: 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리.
    - 특히 순열과 조합 라이브러리는 코딩 테스트에서 자주 사용된다. (완전탐색 문제 등)
- heapq: 힙(Heap) 기능을 제공하는 라이브러리.
    - 일반적으로 우선순위 큐 기능을 구현하기 위해 사용한다.
- bisect: 이진 탐색(Binary Search) 기능을 제공한느 라이브러리다.
- colletions: 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하는 라이브러리다.
- math: 필수적인 수학적 기능을 제공하는 라이브러리다.
    - 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함하고 있다.

## 내장함수

- `sum()`: iterable 객체가 입력으로 주어졌을 때, 모든 원소의 합을 반환한다.파이썬에서 iterable은 반복가능한 객체를 말하며, 리스트, 딕셔너리, 튜플, set 등이 해당한다.
- `max()`: 파라미터가 2개 이상 들어왔을 때 가장 큰 값을 반환한다.
- `min()`: 파라미터가 2개 이상 들어왔을 때 가장 작은 값을 반환한다.
- `eval()`: 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다.
- `sorted()`: iterable 객체가 들어왔을 때, 정렬된 결과를 반환한다.key 속성으로 정렬 기준을 명시할 수 있고, reverse 속성으로 정렬된 결과 리스트를 뒤집을지의 여부를 정할 수 있다.

### `eval()` 사용 예시 소스코드

```python
result = eval("(2 + 4) * 6")
print(result) # 36
```

### `sorted()` 사용 예시 소스코드

```python
result = sorted([9, 3, 2, 7, 4]) # 오름차순으로 정렬
print(result)
# [2, 3, 4, 7, 9]

result = sorted([9, 3, 2, 7, 4], reverse = True) # 내림차순으로 정렬
print(result) 
# [9, 7, 4, 3, 2]
```

파이썬에서 리스트의 원소로 리스트나 튜플이 존재할 때 특정한 기준에 따라서 정렬을 수행할 수 있다.

정렬 기준은 key 속성을 통해 명시한다.

### key 속성 사용 예시

리스트에 튜플이 원소로 있을 때, 이를 튜플의 두 번째 원소를 기준으로 내림차순 정렬하는 예시

```python
result = sorted([('박성재', 27), ('김프론', 33), ('이서버', 42)], key = lambda x: x[1], reverse = True)
print(result)
# [('이서버', 42), ('김프론', 33), ('박성재', 27)]
```

리스트와 같은 iterable 객체는 기본으로 `sort()` 함수를 내장하고 있어서

굳이 `sorted()` 함수를 사용하지 않아도 정렬할 수 있다.

이 경우 리스트 객체의 내부 값이 정렬된 값으로 바로 변경된다.

### `sort()` 함수 예시 소스코드

```python
data = [9 ,3, 2, 5, 6]
data.sort()
print(data)
# [2, 3, 5, 6, 9]
```

## itertools 라이브러리

itertools는 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리이다.

제공하는 클래스는 매우 다양한지만, 코딩 테스트에서 가장 유용하게 사용할 수 있는 클래스는 다음과 같다.

- permutations: 순열
- combinations: 조합
- product: 중복 허용 순열
- combinations_with_replacement: 중복 허용 조합

모두 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하여(or 고려하지 않고)

중복을 허용하여(or 허용하지 않고) 나열하는 모든 경우를 계산한다.

- 데이터 목록과 뽑을 데이터의 개수를 인자로 넘겨준다

모두 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.

### 소스코드

```python
from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C'] # 데이터 준비
result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

result = list(combinations(data, 2)) #2개를 뽑는 모든 조합 구하기
print(result)
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

result = list(combinations_with_replacement(data, repeat=2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
```

## heapq 라이브러리

- 힙(Heap) 기능 제공
- 다익스트라 최단 경로 알고리즘을 비롯한 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용
- PriorityQueue 라이브러리도 사용가능하지만, 코딩 테스트 환경에서 보통 heapq가 더 빠르게 동작
- 파이썬의 힙은 최소 힙으로 구성되어 있어서 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간복잡도 O(NlogN)에 오름차순 정렬이 오나료된다. (보통 최소 힙 자료구조의 최상단 원소는 '가장 작은' 원소이기 때문)
- 힙에 원소를 삽입할 때는 `heap.heappush()` 메서드를 사용
- 힙에서 원소를 꺼재고자 할 때는 `heap.heappop()` 메서드를 사용

### 오름차순 힙정렬 예시 소스코드

```
improt heapq

def heapsort(iterable):
	h = []
    result = []
    # 모든 우너소를 차례대로 힙에 삽입
    for value in iterable:
    	heapq.push(h, vlaue)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내서 담기
   	for i in range(len(h)):
    	result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
```

### 출력

> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

파이썬에서는 최대 힙을 제공하지 않기 때문에, heapq 라이브러리를 이용해서 최대 힙을 구현해야 할 때는 원소의 부호를 임시로 변경하는 방식을 사용한다.힙에 원소를 삽입하기 전에 잠시 부호를 반대로 바꾸었다가, 힙에서 원소를 꺼낸 뒤에 다시 원소의 부호를 바꾸면 된다.

### 내림차순 힙정렬 예시 소스코드

```
import heapq

def heapsort(iterable):
	h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입 (부호 반대로)
    for value in iterable:
    	heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기 (부호 다시 뒤집어서)
    for i in range(len(h)):
    	result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
```

### 출력

> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

## bisect 라이브러리

- 이진 탐색을 쉽게 구현할 수 있도록 해주는 라이브러리
- '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다.
- `bisect_left()`와 `bisect_right()` 함수가 가장 중요하게 사용되며, 이 두 함수가 동작하는 시간 복잡도는 O(logN)이다.
- `bisect_left(a, x)`: 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
- `bisect_right(a, x)`: 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

### 예시 소스코드

```
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
```

### 출력

> 24

위 두 함수는 '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구하고자 할 때, 효과적으로 사용될 수 있다. 시간복잡도는 O(logN)이다.

### 활용 예시 소스코드

```
from bisect import bisect_left, bisect_right

# 값이 [left_vlaue, right_value] 범위에 속하는 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
	right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index
    
# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4)

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3)
```

### 출력

> 26

## collections 라이브러리

- 유용한 자료구조를 제공하는 표준 라이브러리
- 코딩 테스트에서 유용하게 사용되는 클래스는 deque와 Counter이다.

### deque

- 파이썬에서는 보통 deque를 통해 큐를 구현한다.
- 리스트의 경우 맨 뒤에 원소 추가 및 제거의 시간복잡도는 O(1)이지만, 맨 앞에 원소 추가 및 제거는 O(N)이 걸린다.
- deque의 경우 맨 앞과 뒤 모두 원소를 추가하거나 제거할 때 시간복잡도가 O(1)이다.
- deque는 리스트와 다르게 인덱싱, 슬라이싱 기능은 없지만, 연속적으로 나열된 데이터의 시작 부분이나 끝부분에 데이터를 삽입하거나 삭제할 때는 매우 효과적이다.

deque는 데이터의 맨 앞과 맨 뒤 모두에서 삽입과 삭제가 가능하기 때문에 스택으로도 쓸 수 있고, 큐로도 쓸 수 있다.

- 큐로 사용할 때: `popleft()`로 맨 앞 원소 제거, `append(x)`로 맨 뒤에 원소 x 삽입
- 스택으로 사용할 때: `pop()`로 맨 뒤 원소 제거, `append(x)`로 맨 뒤에 원소 x 삽입
- 맨 앞에 원소 x 삽입: `appendleft(x)`

### deque 활용 예시 소스코드

```
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data)) # 리스트 자료형으로 변환

data.popleft()
data.pop()
print(list(data))
```

### 출력

> deque([1, 2, 3, 4, 5])

> [1, 2, 3, 4, 5]

> [2, 3, 4]

### Counter

- 등장 횟수를 세는 기능 제공
- 리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려준다.
- 원소별 등장 횟수를 세는 기능이 필요할 떄 짧은 소스코드로 이를 구현할 수 있다.

### Counter 활용 예시 소스코드

```python
from collections import Counter

counter = Counter(['red', 'blue', 'red' ,'green', 'blue', 'blue'])
print(counter['red']) # 'red'가 등장한 횟수 출력
# 2

print(counter['blue']) # 'blue'가 등장한 횟수 출력
# 3

print(dict(counter)) # 딕셔너리형으로 변환
# {'red': 2, 'blue': 3, 'green': 1}
```

### 

## math 라이브러리

- 자주 사용되는 수학적인 기능을 포함하고 있는 라이브러리
- `factorial(n)`: n!
- `sqrt(x)`: x의 제곱근
- `gcd(a, b)`: a와 b의 최대 공약수
- pi: 상수 파이(pi)
- e: 자연상수 e

### math 활용 예시소스코드

```python
import math

print(math.factorial(5)) # 5 팩토리얼
# 120

print(math.sqrt(6)) # 6의 제곱근 출력
# 2.449489742783178

print(math.gcd(35, 14))
# 7

print(math.pi)
# 3.141592653589793

print(math.e)
# 2.718281828459045
```
