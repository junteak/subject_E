import requests


def show_news():
    response = requests.get('https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty')
    result = response.json()

    print(result)
