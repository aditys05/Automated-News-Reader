# import json
# data ='{"var1":"karikesh", "var2":"pachkawade"}'

# # print(data)
# parsed = json.loads(data)
# # for items in parsed:
# #     print(parsed[items])
# print(parsed)


# import json
# import requests



def speak(str):
    from win32com.client import Dispatch
    sp = Dispatch("SAPI.spvoice")
    sp.Speak(str)
import json
import requests
# speak("Enter your API key")
# apiKey=input("Enter your API key : ")
apiKey = "64882efd57be44d49fdaa8098c97fc40"
url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={apiKey}"
webdata = requests.get(url)

atJson = webdata.json()

# print(atJson['articles'])
a = atJson['articles']
# print(type(a))

for items in a:
        print(f"the news is : \t{items['title']}.") 
        speak(f"The headline is: \n{items['title']}")
speak("this is the end of the news\n thank you for listning \n now you can fuck your wife")
# print(type(a))
# # print(atJson)
# for items in atJson:
#     speak("Reading Articles")
#     # print(atJson.articles[items])
#     # speak(atJson['articles'])

####### json.loads ###########

# import json
# x = '{"name":"kartikesh" , "age":19 , "city":"Amravati"}'
# y = json.loads(x)

# print(y)

######## json.dumps ##########

# a python object dict
# x ={
#     "name":"kartikesh",
#     "age":19,
#     "city":"Amravati"
# }


#               the result is JSON string
# y = json.dumps(x)
# print(y)

#############

#   this json is string
# a =json.dumps({"name":"kartikesh" , "age":19 , "city":"Amravati"})
# print()


#                     ###########@#######$#$#$#$#$#$#$#$#$#$#$
# x = {
#     "name":"kartikesh",
#     "age":19,
#     "married":False,
#     "divorced":False,
#     "commited":True,
#     "childrens":None,
#     "commitsname":"Pratiksha",
#     "skills":[
#         {"skName":"Python" ,"level":"modrate"},
#         {"skName":"Css" ,"level":"intermidiate"}
#     ]
# }

# y = json.dumps(x)
# z = json.loads(y)
# a= z['skills'][1]

# print(type(a))
# a.items()
# print(f"the list is                     :{a}")
# for key,values in a.items():
#     for i in values:
#         print(key ,":", values)
