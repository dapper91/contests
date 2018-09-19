'''
https://practice.geeksforgeeks.org/problems/phone-directory/0
'''

from sys import stdin


def find(words, query):
    result = []

    cur_set = sorted(set(words))
    for i in range(0, len(query)):
        result.append([])

        new_set = []
        for word in cur_set:
            if i < len(word) and word[i] == query[i]:
                result[-1].append(word)
                new_set.append(word)

        cur_set = new_set

    return result


tests = int(stdin.readline())

for _ in range(tests):
    n = int(stdin.readline())

    words = map(lambda w: w.strip(), stdin.readline().split())
    query = stdin.readline().strip()

    for result in find(words, query):
        if result:
            print(" ".join(result))
        else:
            print("0")
