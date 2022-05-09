from itertools import combinations


def solution(orders, course):
    answer = []
    ans_dict = {}

    for order in orders:
        order = sorted(list(order))

        for c in course:
            if c <= len(order):
                combs = combinations(order , c)

                for comb in combs:
                    comb = ''.join(comb)
                    try:
                        ans_dict[comb] += 1
                    except:
                        ans_dict[comb] = 1

    ans_dict = sorted(ans_dict.items(), key = lambda item: item[1], reverse = True)

    res_dict = dict.fromkeys(course, 0) # course:cnt
    for ans in ans_dict:
        print(ans)
        if ans[1] < 2:
            continue
        try:
            if res_dict[len(ans[0])] <= ans[1]:
                res_dict[len(ans[0])] = ans[1]
                answer.append(ans[0])
        except:
            pass

    answer = sorted(answer)
    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

solution(orders, course)