from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *
from .filters import *

from .add_data import add_data
add_data()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        user=User.objects.get(username=serializer.data['username'])
        token=Token.objects.get(user=user)
        response={str(token)}
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)

    # Return ID if user
    def list(self, request, *args, **kwargs):
        try:
            token=request.headers['authorization'][6:]
            userId = Token.objects.get(key=token).user.id
            return Response(userId, status=status.HTTP_200_OK)
        except:
            response = {'message': 'You can\'t use GET method like this'}
            return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)


class RfQuestionBankViewSet(viewsets.ModelViewSet):
    queryset = RfQuestionBank.objects.all()
    serializer_class = RfQuestionBankSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    # Return particular Quiz OR All quiz of request user
    def list(self, request, *args, **kwargs):        
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

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class QuizQuestionBankViewSet(viewsets.ModelViewSet):
    queryset = QuizQuestionBank.objects.all()
    serializer_class = QuizQuestionBankSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )


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


