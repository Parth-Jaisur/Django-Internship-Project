import requests
record = {}
url3 = requests.get("https://inshorts.me/news/all?offset=0&limit=21")
mydata3 = url3.json()
record['sportsdata'] = mydata3

print(record['sportsdata']['data']['articles'][0])
