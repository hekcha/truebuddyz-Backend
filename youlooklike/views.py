from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .filters import *

# from .add_data import add_data
# add_data()


class YouLookLikeViewSet(viewsets.ModelViewSet):
    queryset = YouLookLike.objects.all().order_by('?')
    serializer_class = YouLookLikeSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    # apply filter
    def list(self, request, *args, **kwargs):
        if len(request.query_params) != 1:
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        queryset = self.filter_queryset(self.get_queryset())
        myFilter = YouLookLikeFilter(request.GET, queryset=queryset)
        queryset = myFilter.qs[:10]
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use POST method like this'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use GET method like this'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use PUT method like this'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use DELETE method like this'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)




class YouLookLikeResultViewSet(viewsets.ModelViewSet):
    queryset = YouLookLikeResult.objects.all().order_by('?')
    serializer_class = YouLookLikeResultSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    # apply filter
    def list(self, request, *args, **kwargs):
        if len(request.query_params) != 1:
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        queryset = self.filter_queryset(self.get_queryset())
        myFilter = YouLookLikeResultFilter(request.GET, queryset=queryset)
        queryset = myFilter.qs[:1]
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use POST method like this'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use GET method like this'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use PUT method like this'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use DELETE method like this'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


