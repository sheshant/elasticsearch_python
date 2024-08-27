from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from myapp.documents import ChatGPTTweetsDocument
from myapp.models import ChatGPTTweets
from myapp.serializers import ChatGPTTweetsSerializer


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
