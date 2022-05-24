lotto_price = {
    0 : 6,
    1 : 6,
    2 : 5,
    3 : 4,
    4 : 3,
    5 : 2,
    6 : 1,
}

def solution(lottos, win_nums):
    answer = []
    wins = 0
    zero_wins = 0
    lottos = sorted(lottos, reverse=True)
    for lotto in lottos:
        if lotto in win_nums:
            wins += 1
        elif lotto == 0:
            zero_wins += 1

    zero_wins += wins
    answer = [lotto_price[zero_wins], lotto_price[wins]]

    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = 	[31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))