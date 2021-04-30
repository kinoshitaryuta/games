import tweepy as tweepy
from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models import Post
from django.template.defaultfilters import safe

twitter_auth_keys = {
    "consumer_key": 'EsiRDzxXVskEEjbtSwMkaaNxs',
    "consumer_secret": '0UX5HSEeyk3obzYnKU904aEeIkZI8Qe4AJX5eHdH4yMFMjE19z',
    "access_token": '1225787238224547840-5gt8RXlSr2WvH1cKZ0FlB7K286Yr4t',
    "access_token_secret": 'UmHU6m7L5zERoz6sHTy09JorsmZKNOQl3a62zu9KQRmLb'
}

@receiver(post_save, sender=Post)
def tweet_post(sender, instance, **kwargs):

    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )
    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )
    api = tweepy.API(auth)


    tweet = instance.title + '\n' +'\n' +"https://wewseh.com/"+'\n'+"#WSEH"

    try:
        api.update_status(tweet)
    except tweepy.TweepError as error:
        if error.api_code == 187:
            print('duplicate message')



