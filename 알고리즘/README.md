# 정렬

## sort vs sorted
### sort
리스트를 제자리에서 수정하는 in-place 방식이라 속도가 느리고, 리스트에만 사용할 수 있기 때문에 잘 사용되지 않음
```python
a = [4. 3. 2 .1]
a.sort()
print(a) # [1,2,3,4]
```
### sorted
모든 이터러블에 대해 정렬을 할 수 있는 sorted는 입력으로 받은 값에서 새로운 정렬된 리스트를 반환. 
```python
nums = [4, 3, 2, 1]
sorted_nums = sorted(nums)
print(sorted_nums) # [1,2,3,4]
```
튜플도 동일 
```python
nums = (4, 3, 2, 1])
sorted_nums = sorted(nums)
print(sorted_nums) # [1,2,3,4]
```
딕셔너리의 경우, 키를 기준으로 정렬이 수행됨.
```python
nums = {4: "a", 3: "b", 2:"c", 1:"d"}
sorted_nums = sorted(nums)
print(sorted_nums) # [1,2,3,4]
```
셋도 가능함
```python
nums = {4, 3, 2, 1]}
sorted_nums = sorted(nums)
print(sorted_nums) # [1,2,3,4]
```
문자열은 알파벳 순으로 정렬됨.
```python
string = "dcba"
sorted_string = sorted(string)
print(sorted_nums) # ["a","b","c","d"]
```
## 정렬 응용하기 
### key 로 정렬하기 
```python
names = ["james", "cameroon", "mellon", "indo", "buzzi"]
sorted(names, key =len) # ["indo", "james", "buzzi", "mellon", "cameroon"]
```
### 딕셔너리 정렬
```python
students = {"james": 90, "cameroon":80, "buzzi":70}
```
키를 기준으로 정렬
```python
sorted(students.items())
```
밸류를 기준으로 정렬
```python
sorted(students.itemss(), key = lambda x: x[1])
```
```python
sorted(students, key = lambda x: students[x])
```
여러 기준으로 정렬
튜플을 사용하면 튜플의 첫번째 원소를 기준으로 먼저 정렬한 다음, 값이 같다면 두 번째 원소를 기준으로 다시 정렬함. 여전히 같은 값이 있다면 세 번째 값으로 다시 정렬. 
```python
students = [
  ("james", "A", 100),
  ("cameroon", "B", 70),
  ("buzzi", "A", 100),
  ("buzzi", "A", 90),
  ("buzzi", "C", 30)
]
sorted(students)
```
내림차순 정렬 방법
```python
nums = [1,2,3]
```
reverse=True 파라미터를 추가하면 거꾸로 정렬됨.
```python
sorted(nums, reverse=True)
```
값이 숫자인 경우에 한해서 다음과 같이 람다 함수를 사용할 수도 있음.
```python
sorted(nums, key = lambda x: -x)
```

https://school.programmers.co.kr/learn/courses/30/lessons/42748
https://school.programmers.co.kr/learn/courses/30/lessons/131128
https://school.programmers.co.kr/learn/courses/30/lessons/120886
https://school.programmers.co.kr/learn/courses/30/lessons/120882
https://school.programmers.co.kr/learn/courses/30/lessons/120890
https://school.programmers.co.kr/learn/courses/30/lessons/120835
https://school.programmers.co.kr/learn/courses/30/lessons/12982
https://school.programmers.co.kr/learn/courses/30/lessons/42889

https://school.programmers.co.kr/learn/courses/30/lessons/120837
https://school.programmers.co.kr/learn/courses/30/lessons/42862
https://school.programmers.co.kr/learn/courses/30/lessons/42884

https://school.programmers.co.kr/learn/courses/30/lessons/42895
https://school.programmers.co.kr/learn/courses/30/lessons/42898
https://school.programmers.co.kr/learn/courses/30/lessons/43105
