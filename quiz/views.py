from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *
from .filters import *

from .add_data import add_data
add_data()


class QuizQuestionBankViewSet(viewsets.ModelViewSet):
    queryset = QuizQuestionBank.objects.all().order_by('?')
    serializer_class = QuizQuestionBankSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    # apply filter
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        myFilter = QuizQuestionBankFilter(request.GET,queryset=queryset)
        queryset=myFilter.qs

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


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    # Return particular Quiz OR All quiz of requested user
    def list(self, request, *args, **kwargs):
        try:
            if len(request.query_params)==0:
                token=request.headers['authorization'][6:]
                userId = Token.objects.get(key=token).user.id
                queryset=Quiz.objects.filter(user=userId)
            elif len(request.query_params)==1:
                queryset = self.filter_queryset(self.get_queryset())
                myFilter = QuizFilter(request.GET,queryset=queryset)
                queryset=myFilter.qs
            else:
                response = {'message': 'You can\'t use GET method like this'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except:
            response = {'message': 'Something went wrong'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use GET method like this'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use PUT method like this'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use DELETE method like this'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


class QuizResponseViewSet(viewsets.ModelViewSet):
    queryset = QuizResponse.objects.all()
    serializer_class = QuizResponseSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    # apply filter
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        myFilter = QuizResponseFilter(request.GET,queryset=queryset)
        queryset=myFilter.qs

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use GET method like this'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use PUT method like this'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use DELETE method like this'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

