from collections import deque


def bfs(begin, target, visited, words):
    queue = deque([begin])
    visited[begin] = 1

    while queue:
        word = queue.popleft()

        for i in range(len(word)):
            i_word = word[:i] + word[i+1:]

            try:
                word_list = words[i][i_word]
            except KeyError:
                continue

            for w in word_list:
                if w == target:
                    return visited[word]
                if w == word:
                    continue
                if visited[w] == 0:
                    queue.append(w)
                    visited[w] = visited[word] + 1

    return 0


def solution(begin, target, words):
    answer = 0
    words_dict = {}
    for i in range(len(begin)):
        words_dict[i] = {}
        for word in words:
            i_word = word[:i] + word[i+1:]
            try:
                words_dict[i][i_word].append(word)
            except:
                words_dict[i][i_word] = [word]

    visit_words = {word:0 for word in words}

    answer = bfs(begin, target, visit_words, words_dict)

    return answer


begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", 'cog']

print(solution(begin, target, words))