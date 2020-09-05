import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")

    speak.Speak(str)
if __name__ == '__main__':
    speak("News for today")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=5c91f028bfa04a38a6b72844eee6b3cb"  #TODO:here you can chose your own news website link
    news=requests.get(url).text
    news_dict=json.loads(news)
    print(news_dict["articles"])
    arts=news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to next news listen carefully...")
    speak("Thanks for listening...")




