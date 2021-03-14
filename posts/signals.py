import tweepy as tweepy
from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models import Post
from django.template.defaultfilters import safe

@receiver(post_save, sender=Post)
def tweet_post(sender, instance, **kwargs):
    twitter_auth_keys = {
        "consumer_key": "EIHgOyR712E7u8bHip79vL6Me",
        "consumer_secret": "YsjuqHlQHjScjm5YzB6gVdk4pUO9oG6Dy6ltwdKPnoiPHOgBo8",
        "access_token": "1225787238224547840-GhqFRkoZnrXkuJf2n1fxs7UtslkOBe",
        "access_token_secret": "fITRuVkgXwt0x3Ak5FIWkmXNRKqec4CG96gKGQhXNvnQG"
    }

    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )
    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )
    api = tweepy.API(auth)


    tweet = instance.title + '\n' +'\n' +"#WSEH"

    try:
        api.update_status(tweet)
    except tweepy.TweepError as error:
        if error.api_code == 187:
            print('duplicate message')