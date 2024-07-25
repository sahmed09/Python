import datetime


def matching_words(sentence1, sentence2):
    words1 = sentence1.lower().strip().split(" ")
    words2 = sentence2.lower().strip().split(" ")
    score = 0

    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1 == word2:
                score += 1
    return score


if __name__ == '__main__':
    # print(matching_words("This is good", "Python is good"))
    sentences = ["python is a good", "this is snake", "he is a good boy", "Subscribe to my channel"]
    query = input("Please the query string: ")
    time0 = datetime.datetime.now()
    scores = [matching_words(query, sentence) for sentence in sentences]
    # print(scores)
    sortedSentScore = [sentScore for sentScore in sorted(zip(scores, sentences), reverse=True)
                       if sentScore[0] != 0]  # filtering all space input problem
    print(sortedSentScore)

    print(f"\n{len(sortedSentScore)} results found! in {datetime.datetime.now() - time0} seconds!\n")
    for score, item in sortedSentScore:
        print(f"\"{item}\": with a score of {score}")
