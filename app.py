import requests


def show_news_single():
    response = requests.get('https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty')
    result = response.json()
    single_dic = {'title': result['title'], 'URL': result['url']}

    return single_dic


print(show_news_single())
