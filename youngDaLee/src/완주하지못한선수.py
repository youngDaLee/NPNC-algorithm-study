def solution(participant, completion):
    # make dict
    completion_dict = {}
    for comp in completion:
        try:
            completion_dict[comp] += 1
        except:
            completion_dict[comp] = 1

    for person in participant:
        try:
            if completion_dict[person] > 0:
                completion_dict[person] -= 1
            else:
                return person
        except:
            return person