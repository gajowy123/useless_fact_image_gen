import requests
import flask

def getfact():

    response=requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    data=response.json()
    print(data['text'])
    return data['text']

def getimage(n):
    #response=requests.get(f"https://image.pollinations.ai/prompt/{n}")
    #data=response.json
    #print(response)
    return f"https://image.pollinations.ai/prompt/{n}/width=512&height=512"

def p2i():
    prompt=getfact()
    image=getimage(prompt)
    return image,prompt

