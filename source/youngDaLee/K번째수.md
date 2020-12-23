# 프로그래머스 정렬
- K번째 수
  - https://programmers.co.kr/learn/courses/30/lessons/42748

### 문제 이해하기

### 문제 접근 방법

### 구현 배경 지식
 문제를 풀 당시에는 python에서 list 쓰는 방법을 몰라서 리스트에 공간을 따로 할당했다.   
 하지만 빈 리스트를 할당한 뒤 `.append()` 를 사용하면 오류가 나지 않는다는 것을 알게 되었다.
- python에서 리스트 할당하는 법
  1. 공간할당 뒤 그 자리에 숫자 넣기
    - `li = [0] * n`
    - `li[k] = num`
  2. 빈 리스트 생성 뒤 삽입
    - `li = []`
    - `li.append(num)`
### 접근 방법을 적용한 코드
```
def solution(array, commands):
    answer = [0] * len(commands)
    cnt = 0
    
    for c in commands:
        arr = [0] * (c[1]-c[0]+1)
        
        i_cnt = 0
        for i in range(c[0]-1,c[1]):
            arr[i_cnt] = array[i]
            i_cnt+=1

        arr.sort()

        answer[cnt] = arr[c[2]-1]
        cnt+=1
    
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

arr = solution(array, commands)
print(arr)
```