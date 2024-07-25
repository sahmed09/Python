import wikipedia

wikipedia.set_lang('bn')
result = wikipedia.summary('Bangladesh')
# result = wikipedia.summary('Bangladesh', sentences=50)
print(result)
