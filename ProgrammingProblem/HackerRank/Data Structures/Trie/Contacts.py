from collections import Counter


def contacts(queries):
    ctr = Counter()
    result = []
    for query in queries:
        word = query[1]
        if query[0] == "add":
            for i in range(1, len(word) + 1):
                ctr.update([word[0:i]])
        else:
            result.append(ctr[word])
    # print(ctr)
    return result


if __name__ == '__main__':
    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)
    print(*result, sep="\n")
