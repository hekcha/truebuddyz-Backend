from decouple import config 
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
        if len(request.query_params)!=1: 
            response = {'message': 'You can\'t use POST method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        queryset = self.filter_queryset(self.get_queryset())
        myFilter = YouLookLikeFilter(request.GET,queryset=queryset)
        queryset=myFilter.qs
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        datas=YouLookLikeRandom.objects.all().filter(category=request.query_params['category']).order_by('?')[:6]
        rnadserializer = YouLookLikeRandomSerializer(datas, many=True)
        response = {'message': 'ok','que':serializer.data,'randque':rnadserializer.data}
        return Response(response, status=status.HTTP_200_OK)
        # return Response(serializer.data)

    # add key
    def create(self, request, *args, **kwargs):
        if config('ENCRYPTION_KEY') !=request.headers['encryption']: 
            response = {'message': 'You can\'t use POST method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # add key
    def retrieve(self, request, *args, **kwargs):
        if config('ENCRYPTION_KEY') !=request.headers['encryption']: 
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # add key
    def update(self, request, *args, **kwargs):
        if config('ENCRYPTION_KEY') !=request.headers['encryption']: 
            response = {'message': 'You can\'t use PUT method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    # add key
    def destroy(self, request, *args, **kwargs):
        if config('ENCRYPTION_KEY') !=request.headers['encryption']: 
            response = {'message': 'You can\'t use DELETE method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class YouLookLikeRandomViewSet(viewsets.ModelViewSet):
    queryset = YouLookLikeRandom.objects.all().order_by('?')
    serializer_class = YouLookLikeRandomSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    # add key and apply filter
    def list(self, request, *args, **kwargs):
        if config('ENCRYPTION_KEY') !=request.headers['encryption']: 
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        queryset = self.filter_queryset(self.get_queryset())
        myFilter = YouLookLikeRandomFilter(request.GET,queryset=queryset)
        queryset=myFilter.qs

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # add key
    def create(self, request, *args, **kwargs):
        if config('ENCRYPTION_KEY') !=request.headers['encryption']: 
            response = {'message': 'You can\'t use POST method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # add key
    def retrieve(self, request, *args, **kwargs):
        if config('ENCRYPTION_KEY') !=request.headers['encryption']: 
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # add key
    def update(self, request, *args, **kwargs):
        if config('ENCRYPTION_KEY') !=request.headers['encryption']: 
            response = {'message': 'You can\'t use PUT method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    # add key
    def destroy(self, request, *args, **kwargs):
        if config('ENCRYPTION_KEY') !=request.headers['encryption']: 
            response = {'message': 'You can\'t use DELETE method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class YouLookLikeScoreViewSet(viewsets.ModelViewSet):
    queryset = YouLookLikeScore.objects.all()
    serializer_class = YouLookLikeScoreSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        myFilter = YouLookLikeScoreFilter(request.GET,queryset=queryset)
        queryset=myFilter.qs
        if len(queryset)==0:
            cat = request.GET['category']
            queryset=YouLookLikeScore.objects.filter(category=cat).order_by('?')[:1]

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # add key
    def create(self, request, *args, **kwargs):
        if config('ENCRYPTION_KEY') !=request.headers['encryption']: 
            response = {'message': 'You can\'t use POST method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # add key
    def retrieve(self, request, *args, **kwargs):
        if config('ENCRYPTION_KEY') !=request.headers['encryption']: 
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # add key
    def update(self, request, *args, **kwargs):
        if config('ENCRYPTION_KEY') !=request.headers['encryption']: 
            response = {'message': 'You can\'t use PUT method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    # add key
    def destroy(self, request, *args, **kwargs):
        if config('ENCRYPTION_KEY') !=request.headers['encryption']: 
            response = {'message': 'You can\'t use DELETE method like this'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
