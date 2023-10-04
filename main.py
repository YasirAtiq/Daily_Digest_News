import requests
from send_email import send_mail

api_key = "7cb08aeed3fc44feb476188870547c64"
url = (f"https://newsapi.org/v2/everything?"
       f"q=tesla&from=2023-09-04&sortBy=publishedAt&apiKey={api_key}")

request = requests.get(url)
content = request.json()

email_body = ""
for article in content["articles"]:
    email_body = email_body + f"{article['title']} \n" + article["description"] + 2*"\n"

send_mail("Today's Tesla News", message=email_body)
