import json
from requests_oauthlib import OAuth1Session
# --ログツール------------------------------------------
import logging


# logging.debug('hi_debug')

class TwitterApi:
    def __init__(self, oauth_session_params):
        CONSUMER_KEY = oauth_session_params['consumer_key']
        CONSUMER_SECRET = oauth_session_params['consumer_secret']
        ACCESS_TOKEN = oauth_session_params['access_token']
        ACCESS_SECRET = oauth_session_params['access_secret']
        self.twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
        self.url_trend = "https://api.twitter.com/1.1/trends/place.json"
        self.url_search = "https://api.twitter.com/1.1/search/tweets.json"
        self.url_embed = "https://publish.twitter.com/oembed"
        self.url_status = "https://api.twitter.com/1.1/statuses/show.json"

    def search_tweets(self, keyword, count):
        params = {'q': keyword, 'count': count}
        request = self.twitter.get(self.url_search, params=params)
        if request.status_code == 200:
            search_tweets = json.loads(request.text)
            return search_tweets

    def get_tweet_ids(self, search_tweets):
        tweet_ids = []
        for tweet in search_tweets['statuses']:
            tweet_ids.append(str(tweet['id']))
        return tweet_ids

    def get_screen_names(self, tweet_ids):
        embed_params_dicts = []
        for tweet_id in tweet_ids:
            params = {'id': tweet_id}
            request = self.twitter.get(self.url_status, params=params)
            status = json.loads(request.text)
            screen_name = status['user']['screen_name']
            embed_params_dict = {}
            embed_params_dict['tweet_id'] = tweet_id
            embed_params_dict['screen_name'] = screen_name
            embed_params_dicts.append(embed_params_dict)
        return embed_params_dicts

    def get_embed_datas(self, embed_params_dicts):
        embed_datas = []
        for e in embed_params_dicts:
            url = 'https://twitter.com/' + e['screen_name'] + '/' + 'status/' + e['tweet_id']
            params = {'url': url, 'hide_media': False, 'align': 'center'}
            request = self.twitter.get(self.url_embed, params=params)
            embed_data = json.loads(request.text)
            embed_datas.append(embed_data['html'])
        return embed_datas

    def get_tweets(self, keyword, count):
        search_tweets = self.search_tweets(keyword, count)
        tweet_ids = self.get_tweet_ids(search_tweets)
        embed_params_dicts = self.get_screen_names(tweet_ids)
        embed_datas = self.get_embed_datas(embed_params_dicts)
        return embed_datas