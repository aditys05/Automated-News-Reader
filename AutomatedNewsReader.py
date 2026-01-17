import requests
import pyttsx3

def speak(text):
   engine = pyttsx3.init()
   engine.say(text)
   engine.runAndWait()


apiKey = "YOUR_NEWSAPI_KEY"
URL = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={apiKey}"

response = requests.get(URL)

data = response.json()


articles = data.get('articles', [])  

if not articles:
    print("No Technological news articles found.")
    speak("No Technological news articles found.")
else:
    print("Latest Technological news:\n")
    speak("Here are the latest technological news headlines for you.")


    for article in articles:
        title = article.get("title")
        if title:
            print(f"Headline : {title}") 
        speak(f"- {title}")

speak("This is the end of the news\n thank you for listning \n Now you have a Good Day and Good Night")

