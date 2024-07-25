from win32com.client import Dispatch  # install pywin32
import requests
import json


# def speak(string):
#     speak = Dispatch("SAPI.SpVoice")
#     speak.Speak(string)


if __name__ == '__main__':
    # speak("News for today: ")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=f2dab0ce395f4770bd125a336158fca2"

    news = requests.get(url).text
    news_json = json.loads(news)

    # print(news_json["articles"])  # printing all articles

    arts = news_json['articles']
    # print(len(arts))

    i = 1
    for article in arts:
        print(article['title'])
        # speak(article['title'])
        print("To read more: ", article['url'], "\n")
        i += 1
        # if len(article['title']) != 0:
    #     if i == len(arts):
    #         speak("So our last news for today is ")
    #     else:
    #         speak("Moving to our next News..")
    #
    # speak("Thanks for listening...")
