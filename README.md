[TOC]

# 0. Hello!
- 아래의 목적의 repo 입니다.
    - 온라인 저지 정답 코드
    - 코드 이해를 위한 간단한 가이드

## 0.1 개선 예정 사항
- [ ] 자주 쓰는 코드 라이브러리 만들기
- [ ] baekjoon 실행 및 테스트 환경 만들기
  - 실행 시간 측정
  - 테스트 케이스 추가 가능하도록
- [ ] 자주 쓰이는 수학 공식 정리

# 1. Python Cheatsheet
- 파이썬 문법 관련

## 1.1 Syntax

### 1.1.1 조건문

### 1.1.2 반복문
```python
for var in iterator :
    print(var)
```

### 1.1.3 전역변수 사용하기
```python
글로벌로_사용할_변수 = "something"
# 함수 내부에서 
def some_function(parameter):
    global 글로벌로_사용할_변수
    print(글로벌로_사용할_변수) # something 
```

### 1.1.4 Built-In Functions
- range()
- int()
- print()
- input()
- enumerate()
- sort()
- sorted()
- map()
- list()
- divmod()
  - <https://programmers.co.kr/learn/courses/4008/lessons/12732>

## 1.2 Style(for Java Developer)
- 파이썬에서는 함수(메서드)와 변수에 snake_case를 사용한다.
- 클래스에는 PascalCase를 사용한다.
- 따라서 표기 형식만 보고도 변수인지, 함수인지, 클래스인지 어느정도 짐작할 수 있다.
    - snake_case에 파라미터가 없으면 변수겠거니..


# 2. Algorithm

- BOJ
- 프로그래머스
- HackerRank
- Codility

## 2.1 단계별 참고
### 2.1.1 기초
#### 2.1.1.1 백준 온라인 강의
- 알고리즘 기초 1/2 : <https://code.plus/course/41>
  - [x] 300 수학 1
  - [ ] 301 수학 1 연습
  - [ ] 303 수학 1 (참고)
- 알고리즘 기초 2/2 : <https://code.plus/course/42>

## 2.2 항목별

### 2.2.1 Greedy

### 2.2.3 DFS/BFS

#### 백준 분류 태그 리스트
- [깊이 우선 탐색](https://www.acmicpc.net/problemset?sort=ac_desc&algo=127)

#### 푼 문제
- <https://www.acmicpc.net/problem/2667>
- <https://www.acmicpc.net/problem/2606>
- <https://www.acmicpc.net/problem/1260>

### 2.2.2 Dynamic
- <https://www.acmicpc.net/problem/9095>
    - 참고 : <https://sihyungyou.github.io/baekjoon-9095/>