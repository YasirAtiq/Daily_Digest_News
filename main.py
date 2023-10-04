import requests

api_key = "7cb08aeed3fc44feb476188870547c64"
url = (f"https://newsapi.org/v2/everything?"
       f"q=tesla&from=2023-09-04&sortBy=publishedAt&apiKey={api_key}")

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
