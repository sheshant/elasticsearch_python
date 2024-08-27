from rest_framework import serializers
from myapp.models import ChatGPTTweets


class ChatGPTTweetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatGPTTweets
        fields = '__all__'

