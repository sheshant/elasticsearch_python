from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from myapp.documents import ChatGPTTweetsDocument
from myapp.models import ChatGPTTweets
from myapp.serializers import ChatGPTTweetsSerializer
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend, SearchFilterBackend,
)


class Search(APIView):
    permission_classes = IsAuthenticated,

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        results = ChatGPTTweetsDocument.search().query("match", content=query).execute()
        return Response(
            [
                {
                    "id": result.id,
                    "date": result.date,
                    "content": result.content,
                    "username": result.username
                }
                for result in results
            ]
        )


class ChatGPTTweetsDocumentView(DocumentViewSet):
    document = ChatGPTTweetsDocument
    serializer_class = ChatGPTTweetsSerializer
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]

    # Define search fields
    search_fields = (
        'content',
        'username',
    )

    # Define filter fields
    filter_fields = {
        'username': 'username.raw',
        'id': 'id.raw',
    }

    # Define ordering fields
    ordering_fields = {
        'date': 'date',
    }

    # Specify default ordering
    ordering = ('-date',)


class ChatGPTTweetsView(ListCreateAPIView):
    serializer_class = ChatGPTTweetsSerializer
    pagination_class = PageNumberPagination
    permission_classes = IsAuthenticated,
    queryset = ChatGPTTweets.objects.all()


class ChatGPTTweetsSingleView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChatGPTTweetsSerializer
    pagination_class = PageNumberPagination
    permission_classes = IsAuthenticated,
    queryset = ChatGPTTweets.objects.all()
    lookup_field = "id"
