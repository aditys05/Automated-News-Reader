
def speak(str):
    from win32com.client import Dispatch
    sp = Dispatch("SAPI.spvoice")
    sp.Speak(str)
import json
import requests

apiKey = "64882efd57be44d49fdaa8098c97fc40"
url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={apiKey}"
webdata = requests.get(url)

atJson = webdata.json()


a = atJson['articles']


for items in a:
        print(f"the news is : \t{items['title']}.") 
        speak(f"The headline is: \n{items['title']}")
speak("this is the end of the news\n thank you for listning \n now you have a good day and good night")

