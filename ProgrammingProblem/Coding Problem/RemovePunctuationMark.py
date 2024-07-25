punctuation = '''''!()-[]{};:'",<>./?@#$%^&*_~'''

text = "Hello... this is a encrypted (@#$&,,) keyword"

no_punct = ""

for char in text:
    if char not in punctuation:
        no_punct = no_punct + char

print(no_punct)
