from textblob import TextBlob  # pip install textblob

word_list = ["incorret", "spell"]
corrected_list = []

for word in word_list:
    corrected_list.append(TextBlob(word))

print("Corrected word list:")
for word in corrected_list:
    print(word.correct(), end=" ")
