# 비선형 자료구조

## 힙
### 힙 파이썬 구현 
```python
import heapq
nums = [1,3,5,7,9,2,4,6,8,0]
heapq.heapify(nums)
print(nums)
```

```python
import heapq

def heapsort(iterable):
  h = []
  for value in iterable:
    heapq.heappush(h, value)
  return [heapq.heappop(h)[1] for _ in range(len(h))]
print(heapsort([1,3,5,7,9,2,4,6,8,0])) # [9,8,7,6,5,4,3,2,1]
```

### 우선 순위 큐
```python
import heapq
students = [
  (2, "cameroon"),
  (3, "buzzi"),
  (1, "james"),
  (5, "mellon"),
  (4, "indo")
]
heap = []
for student in students:
  heapq.heappush(heap, student)
while heap:
  print(heapq.heappop(heap))
```



## 프로그래머스 문제 
https://school.programmers.co.kr/learn/courses/30/lessons/138477
https://school.programmers.co.kr/learn/courses/30/lessons/42626
https://school.programmers.co.kr/learn/courses/30/lessons/12927

https://school.programmers.co.kr/learn/courses/30/lessons/12943
https://school.programmers.co.kr/learn/courses/30/lessons/43164
https://school.programmers.co.kr/learn/courses/30/lessons/43162

https://school.programmers.co.kr/learn/courses/30/lessons/43165
https://school.programmers.co.kr/learn/courses/30/lessons/1844
