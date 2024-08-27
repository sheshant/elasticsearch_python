from django.db import models


class Tweets(models.Model):
    keyword = models.CharField(null=True, max_length=1000)
    location = models.CharField(null=True, max_length=1000)
    text = models.TextField(null=True, default=None)
    target = models.BooleanField(null=False, default=False)


class ChatGPTTweets(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    date = models.DateTimeField(null=True, auto_now_add=True)
    content = models.TextField(null=True, default=None)
    username = models.CharField(null=True, max_length=1000)
    like_count = models.PositiveIntegerField(null=True)
    retweet_count = models.PositiveIntegerField(null=True)
