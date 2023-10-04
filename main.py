import requests
from send_email import send_mail

## Adding which topic to receive news on
topic = "tesla"

## Adding url
api_key = "7cb08aeed3fc44feb476188870547c64"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2023-09-04&"
       "sortBy=publishedAt&"
       f"apiKey={api_key}&"
       "language=en")

## Getting API
request = requests.get(url)
content = request.json()

## Adding the news to the email
email_body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        email_body = (email_body + article['title'] + "\n" +
                      article["description"] + "\n" + article['url'] +
                      2 * "\n")

## Sending the email with "Today's Tesla News" as the subject
send_mail(subject="Today's Tesla News", message=email_body)
