
from django.urls import path


from myapp.views import Search, ChatGPTTweetsView, ChatGPTTweetsSingleView, ChatGPTTweetsDocumentView

urlpatterns = [
    path("search/", Search.as_view(), name="search"),
    path("search/chat_gpt_tweets/", ChatGPTTweetsDocumentView.as_view({'get': 'list'}), name="search_chat_gpt_tweets"),
    path("chat_gpt_tweets/", ChatGPTTweetsView.as_view(), name="chat_gpt_tweets"),
    path('chat_gpt_tweets/<int:id>/', ChatGPTTweetsSingleView.as_view(), name="chat_gpt_tweets_single"),
]
