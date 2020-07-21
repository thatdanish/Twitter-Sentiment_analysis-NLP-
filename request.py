import requests

url = 'http://127.0.0.1:5000/predict'
url2 = 'https://api.github.com/'
r = requests.post(url, json={'text':"YO, What's Up!! How's going my man!!"}).json()


if r['success']:
    print(r['prediction'])
else:
    print("POST Request Failed!!")
    print("Check Server For Error And Try Again.")