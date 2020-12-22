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

## 1.1 Basic Syntax

## 1.1.0 Style(for Java Developer)
- 파이썬에서는 함수(메서드)와 변수에 snake_case를 사용한다.
- 클래스에는 PascalCase를 사용한다.
- 따라서 표기 형식만 보고도 변수인지, 함수인지, 클래스인지 어느정도 짐작할 수 있다.
    - snake_case에 파라미터가 없으면 변수겠거니..

### 1.1.1 리스트
- 리스트에 원소를 추가할 때 : `append()`
- 리스트에 리스트 자체의 원소를 추가할 때 : `extend()` 
- `pop()`
    - <https://brownbears.tistory.com/452>
#### 1.1.1.1 리스트 슬라이싱
- 시작부터 끝
    ```python
    list[start:end]
    ```
- 스텝을 추가
    ```python
    list[start:end:step]
    ```
- 각 값을 생략 가능하다.

### 1.1.2 조건문

### 1.1.3 반복문
- 반복문 기본 형태
    ```python
    for var in iterator :
        print(var)
    ```

### 1.1.4 전역변수 사용하기
```python
글로벌로_사용할_변수 = "something"
# 함수 내부에서 
def some_function(parameter):
    global 글로벌로_사용할_변수
    print(글로벌로_사용할_변수) # something 
```

## 1.2 Built-In Functions
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
- join()

### 1.2.1 미분류
- 순열 조합
```python
from itertools import permutations
from itertools import combinations
```

## 1.3 Library


# 2. Algorithm

- 에라토스테네스의 체


# 3. Reference

## 3.1 온라인 저지 사이트
- BOJ
- 프로그래머스
- HackerRank
- Codility

## 3.2 단계별 참고용 리스트

### 3.2.1 기초

#### 3.2.1.1 백준 온라인 강의(CodePlus)
##### 3.2.1.1.1 알고리즘 기초 1/2 : <https://code.plus/course/41>
  - [ ] 200 자료구조 1
    - [x] [스택](https://www.acmicpc.net/problem/10828)
    - [x] [단어 뒤집기](https://www.acmicpc.net/problem/9093)
    - [x] [괄호](https://www.acmicpc.net/problem/9012)
    - [x] [스택 수열](https://www.acmicpc.net/problem/1874)
    - [ ] [에디터](https://www.acmicpc.net/problem/1406)
    - [ ] [큐](https://www.acmicpc.net/problem/10845)
    - [ ] [조세퍼스 문제](https://www.acmicpc.net/problem/1158)
    - [ ] [덱](https://www.acmicpc.net/problem/10866)
  - [ ] 201 자료구조 1(연습)
    - [ ] [단어 뒤집기 2](https://www.acmicpc.net/problem/17413)
    - [ ] [쇠막대기](https://www.acmicpc.net/problem/10799)
    - [ ] [오큰수](https://www.acmicpc.net/problem/17298)
    - [ ] [오등큰수](https:
  - [ ] 203 자료구조 1(참고)
    - [ ] [후위 표기식2](https://www.acmicpc.net/problem/1935)
    - [ ] [후위 표기식](https://www.acmicpc.net/problem/1918)
    - [ ] [알파벳 개수](https://www.acmicpc.net/problem/10808)
    - [ ] [알파벳 찾기](https://www.acmicpc.net/problem/10809)
    - [ ] [문자열 분석](https://www.acmicpc.net/problem/10820)
    - [ ] [단어 길이 재기](https://www.acmicpc.net/problem/2743)
    - [ ] [ROT13](https://www.acmicpc.net/problem/11655)
    - [ ] [네 수](https://www.acmicpc.net/problem/10824)
    - [ ] [접미사 배열](https://www.acmicpc.net/problem/11656)
  - [x] 300 수학 1
    - [x] [나머지](https://www.acmicpc.net/problem/10430)
    - [x] [최대공약수와 최소공배수](https://www.acmicpc.net/problem/2609)
    - [x] [최소공배수](https://www.acmicpc.net/problem/1934)
    - [x] [소수 찾기](https://www.acmicpc.net/problem/1978)
    - [x] [소수 구하기](https://www.acmicpc.net/problem/1929)
    - [x] [골드바흐의 추측](https://www.acmicpc.net/problem/6588)
    - [x] [팩토리얼](https://www.acmicpc.net/problem/10872)
    - [x] [팩토리얼 0의 개수](https://www.acmicpc.net/problem/1676)
    - [x] [조합 0의 개수](https://www.acmicpc.net/problem/2004)
  - [x] 301 수학 1 연습
    - [x] [GCD 합](https://www.acmicpc.net/problem/9613)
    - [x] [숨바꼭질 6](https://www.acmicpc.net/problem/17087)
    - [x] [2진수 8진수](https://www.acmicpc.net/problem/1373)
    - [x] [8진수 2진수](https://www.acmicpc.net/problem/1212)
    - [x] [-2진수](https://www.acmicpc.net/problem/2089)
    - [x] [골드바흐 파티션](https://www.acmicpc.net/problem/17103)
  - [x] 303 수학 1 (참고)
    - [x] [진법 변환 2](https://www.acmicpc.net/problem/11005)
    - [x] [진법 변환](https://www.acmicpc.net/problem/2745)
    - [x] [Base Conversion](https://www.acmicpc.net/problem/11576)
    - [x] [소인수분해](http
  - [ ] 400 다이나믹 프로그래밍 1
    - [ ] [1로 만들기](https://www.acmicpc.net/problem/1463)
    - [ ] [2×n 타일링](https://www.acmicpc.net/problem/11726)
    - [ ] [2×n 타일링 2](https://www.acmicpc.net/problem/11727)
    - [ ] [1, 2, 3 더하기](https://www.acmicpc.net/problem/9095)
    - [ ] [카드 구매하기](https://www.acmicpc.net/problem/11052)
    - [ ] [카드 구매하기 2](https://www.acmicpc.net/problem/16194)
    - [ ] [1, 2, 3 더하기 5](https://www.acmicpc.net/problem/15990)
    - [ ] [쉬운 계단 수](https://www.acmicpc.net/problem/10844)
    - [ ] [이친수](https://www.acmicpc.net/problem/2193)
    - [ ] [가장 긴 증가하는 부분 수열](https://www.acmicpc.net/problem/11053)
    - [ ] [가장 긴 증가하는 부분 수열 4](https://www.acmicpc.net/problem/14002)
    - [ ] [연속합](https://www.acmicpc.net/problem/1912)
    - [ ] [제곱수의 합](https://www.acmicpc.net/problem/1699)
    - [ ] [합분해](https://www.acmicpc.net/problem/2225)
  - [ ] 401 다이나믹 프로그래밍 1 (연습)
    - [ ] [1, 2, 3 더하기 3](https://www.acmicpc.net/problem/15988)
    - [ ] [RGB거리](https://www.acmicpc.net/problem/1149)
    - [ ] [동물원](https://www.acmicpc.net/problem/1309)
    - [ ] [오르막 수](https://www.acmicpc.net/problem/11057)
    - [ ] [스티커](https://www.acmicpc.net/problem/9465)
    - [ ] [포도주 시식](https://www.acmicpc.net/problem/2156)
    - [ ] [정수 삼각형](https://www.acmicpc.net/problem/1932)
    - [ ] [가장 큰 증가 부분 수열](https://www.acmicpc.net/problem/11055)
    - [ ] [가장 긴 감소하는 부분 수열](https://www.acmicpc.net/problem/11722)
    - [ ] [가장 긴 바이토닉 부분 수열](https://www.acmicpc.net/problem/11054)
    - [ ] [연속합 2](https://www.acmicpc.net/problem/13398)
    - [ ] [타일 채우기](https://www.acmicpc.net/problem/2133)
  - [ ] 402 다이나믹 프로그래밍 1 (도전)
    - [ ] [동물원](https://www.acmicpc.net/problem/1309)
    - [ ] [RGB거리 2](https://www.acmicpc.net/problem/17404)
    - [ ] [합분해](https://www.acmicpc.net/problem/2225)

##### 3.2.1.1.2 알고리즘 기초 2/2 : <https://code.plus/course/42>

## 3.2 항목별
- 디렉토리 구조 참고

### 3.2.1  백준 분류 태그 리스트
- [깊이 우선 탐색](https://www.acmicpc.net/problemset?sort=ac_desc&algo=127)