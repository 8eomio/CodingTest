# 기초 

### 문자열 조작 함수 

## 문자 개수 새기 (count)

```python
a = "hobby"
a,count = ('b') # 2
```
문자열 중 문자 b의 개수를 돌려줌.

### 위치 알려주기(find)

```python
a = "Python is the best choice"
a.find('b') # 14
a.find('k') # -1
```
문자열 중 문자 b가 처음으로 나온 위치를 반환함. 만약 찾는 문자나 문자열이 존재하지 않는다면 -1 반환 

### 위치 알려주기2(index)
```python
a = "Life is too short"
a.index('t') # 8
a.index('k')
'''
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: substring not found
'''
```
문자열 중 문자 t가 가장 처음으로 나온 위치를 반환함. 만약 찾는 문자나 문자열이 존재하지 않는다면 ValueError 오류를 발생시킴. 앞의 find 함수와 다른 점은, 문자열 안에 존재하지 않는 문자를 찾으면 오류가 발생한다는 점.

### 문자열 삽입(join)
주어진 리스트, 튜플, 문자열의 원소를 입력으로 받아서 각 원소 사이에 주어진 문자열을 삽입하는 함수. 아래 예제에서는 'abcd' 문자열의 각 문자 사이에 문자열 , 를 삽입함. 
```python
",".join('abcd') # a,b,c,d
```
join 함수의 입력으로 리스트를 사용하는 예:
```python
",".join(['a', 'b', 'c', 'd') # a,b,c,d
```

### 소문자를 대문자로 바꾸기(upper)
```python
a = "hi"
a.upper() # "HI"
```
upper 함수는 소문자를 대문자로 바꾸어 줌. 만약 어떤 문자가 이미 대문자라면 아무 변화도 일어나지 않음. 

### 대문자를 소문자로 바꾸기(lower)
```python
a = "HI"
a.lower() # "hi"
```

### 왼쪽 공백 지우기(lstrip) 
```python
a = " hi "
a.lstrip() # "hi "
```

### 오른쪽 공백 지우기(rstrip) 
```python
a = " hi "
a.rstrip() # "hi"
```

### 양쪽 공백 지우기(strip) 
```python
a = " hi "
a.strip() # "hi"
```

### 문자열 바꾸기(replace)
```python
a = "Life is too short"
a.replace("Life", "Your leg") # Your leg is too short!
```
replace(바뀌게 될 문자열, 바꿀 문자열)처럼 사용함. 문자열 안의 특정한 값을 다른 값으로 치환해 줌. 추가적으로 세 번째 파라미터로 몇 번 지울지를 지정 가능
```python
string = "Butter"
print(string.replace("t", "m")) # Bummer
print(string.replace("t", "m", 1)) # Bumter
```

### 문자열 나누기(split)
split 함수는 a.split()처럼 괄호 안에 아무 값도 넣어 주지 않으면 공백 문자(스페이스, 탭, 엔터 등)를 기준으로 문자열을 나누어 리스트로 만들어 줍니다. 
```python
a = "Life is too short"
a.stlit() # ['Life', 'is', 'too', 'short']
```
만약 b.split(':')처럼 괄호 안에 특정 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나누게 됨. 
```python
b = "a:b:c:d"
b.split(':') # ['a', 'b', 'c', 'd']
```

### 문자가 숫자인지 검사
isdigit은 특정 문자열이 숫자로만 구성되어 있는지를 검사함. 만일 숫자로만 구성되어 있다면 True를, 아니라면 False를 리턴함.
```python
s = "2023"
print(s.isdigit()) # True
```
코딩테스트에서는 주로 문자열의 문자 한 개가 숫자인지를 검사하는 데 자주 사용함.
```python
s = "4 July"
for char in s:
	print(char.isdigit(), end = " ")
# True False False False False False
```
isdigit: 문자열의 모양이 숫자처럼 생겼다면 숫자로 변환
isnumeric: isdigit + 로마숫자 변환 
isdecimal: 정수 형태의 10진수 변환 

### 문자가 알파벳/한글 또는 숫자인지 검사( isalnum)
isalnum은 어떤 문자가 알파벳 또는 숫자인지를 검사하는 메소드로, alphanumeric이라는 단어를 줄여서 만든 이름. 하지만 실제로는 문자가 한글이어도 True가 반환됨.
```python
s = "안녕, Python3"
for char in s:
	print(char.isalnum(), end = " ")
#True True False False True True True Ture True True True
```

### 문자열을 아스키 코드값으로(ord), 아스키 코드값을 문자열으로(chr)
파이썬의 ord() 및 chr 함수는 문자와 해당 유니코드 코드 포인트 간에 변환하는데 사용함. 하지만 실제로 코딩테스트에서 대부분은 숫자나 알파벳으로 이루어진 문자열이 주어짐. 이모티콘이나 한글 같은 유니코드 문자는 잘 주어지지 않기 때문에, 여기서는 주어진 문자열을 아스키 코드값으로 그리고아스키 코드값을 문자열로 바꾸는 함수라고 기억해도 무방함. 
ord() 함수는 문자 하나를 입력받아 해당 문자의 아스키 코드값을 나타내는 정수를 리턴함. 예를 들어, ord('A')는 대문자 'A'의 아스키 코드값인 65를 리턴함. 
```python
char = 'A'
code_print = ord(char)
print(code_print) # 출력: 65
```
반면에 chr() 함수는 아스키 코드값을 입력받아 코드에 해당하는 문자를 반환함. 예를 들어, chr(65)는 문자 'A'를 반홤함.
```python
new_char = chr(code_print)
print(new_char) # 출력: A
```
### 프로그래머스 문제 
[옹알이(1)](https://school.programmers.co.kr/learn/courses/30/lessons/120956) </br>
[문자열 계산하기](https://school.programmers.co.kr/learn/courses/30/lessons/120902) </br>
[OX퀴즈](https://school.programmers.co.kr/learn/courses/30/lessons/120907) </br>
[숨어있는 숮자의 덧셈](https://school.programmers.co.kr/learn/courses/30/lessons/120864) </br>
[인덱스 바꾸기](https://school.programmers.co.kr/learn/courses/30/lessons/120895) </br>
(https://school.programmers.co.kr/learn/courses/30/lessons/120921) </br>
(https://school.programmers.co.kr/learn/courses/30/lessons/140108) </br>
[옹알이(2)](https://school.programmers.co.kr/learn/courses/30/lessons/133499) </br>
