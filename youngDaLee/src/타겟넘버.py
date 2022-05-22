"""
numbers = [4,1,2,1]
target = 4
인 경우 시나리오

dfs([-4], [1,2,1], 4, 4)
    -> dfs([-4,-1], [2,1], 4, 4)
        -> dfs([-4,-1,-2], [1], 4, 4)
            -> dfs([-4,-1,-2,-1], [], 4, 4) => 0
            -> dfs([-4,-1,-2,1], [], 4, 4) => 0
        -> dfs([-4,-1,2], [1], 4, 4)
            -> dfs([-4,-1,2,-1], [], 4, 4) => 0
            -> dfs([-4,-1,2,1], [], 4, 4) => 0
    -> dfs([-4,1], [2,1], 4, 4)
        -> dfs([-4,1,-2], [1], 4, 4)
            -> dfs([-4,1,-2,-1], [], 4, 4) => 0
            -> dfs([-4,1,-2,1], [], 4, 4) => 0
        -> dfs([-4,1,2], [1], 4, 4)
            -> dfs([-4,1,2,-1], [], 4, 4) => 0
            -> dfs([-4,1,2,1], [], 4, 4) => 0
dfs([4], [1,2,1], 4, 4)
    -> dfs([4,-1], [2,1], 4, 4)
        -> dfs([4,-1,-2], [1], 4, 4)
            -> dfs([4,-1,-2,-1], [], 4, 4) => 0
            -> dfs([4,-1,-2,1], [], 4, 4) => 0
        -> dfs([4,-1,2], [1], 4, 4)
            -> dfs([4,-1,2,-1], [], 4, 4) => 1
            -> dfs([4,-1,2,1], [], 4, 4) => 0
    -> dfs([4,1], [2,1], 4, 4)
        -> dfs([4,1,-2], [1], 4, 4)
            -> dfs([4,1,-2,-1], [], 4, 4) => 0
            -> dfs([4,1,-2,1], [], 4, 4) => 1
        -> dfs([4,1,2], [1], 4, 4)
            -> dfs([4,1,2,-1], [], 4, 4) => 0
            -> dfs([4,1,2,1], [], 4, 4) => 0

=> res = 2
"""
def dfs(array, numbers, target, size):
    answer = 0
    if len(array) == size:  # 조사 끝난 경우
        if sum(array) == target:
            return 1
        else:
            return 0
    else:
        num = numbers.pop(0)
        for i in [-1, 1]:  # num이 음수/양수인 경우 재귀적으로 조사
            array.append(num*i)
            answer += dfs(array, numbers, target, size)
            array.pop()
        numbers.append(num)
        return answer

def solution(numbers, target):
    answer += dfs([numbers[0]], numbers[1:], target, len(numbers))
    answer += dfs([-numbers[0]], numbers[1:], target, len(numbers))
    return answer