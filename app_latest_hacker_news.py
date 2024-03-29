'''

Hacker News
https://news.ycombinator.com/newest
API
https://github.com/HackerNews/API

'''

import time

import requests

print('\nThe latest 10 articles of Hacker News\n')

def show_news():
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
    result = response.json()  # latestの辞書

    i = 0

    for i in range(0, 11):
        num = result[i]
        time.sleep(1)
        response_latest = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{num}.json?print=pretty')
        show = response_latest.json()
        dic = {'title': show['title'], 'URL': show['url']}
        print(dic)


show_news()
