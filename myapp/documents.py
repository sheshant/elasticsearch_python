from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import ChatGPTTweets


@registry.register_document
class ChatGPTTweetsDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'chatgpt_tweets_index'
        # Settings for the index
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = ChatGPTTweets  # The model associated with this Document

        # Fields of the model to be indexed
        fields = [
            "id",
            "date",
            "content",
            "username",
        ]
