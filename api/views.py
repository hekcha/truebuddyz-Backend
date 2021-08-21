from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
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
    queryset = RfQuestionBank.objects.all().order_by('?')
    serializer_class = RfQuestionBankSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        myFilter = RfQuestionBankFilter(request.GET,queryset=queryset)
        queryset=myFilter.qs

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class QuizQuestionBankViewSet(viewsets.ModelViewSet):
    queryset = QuizQuestionBank.objects.all().order_by('?')
    serializer_class = QuizQuestionBankSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )
    
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

    @action(detail=False, methods=['GET'])
    def entertainment(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        myFilter = QuizQuestionBankFilter(request.GET,queryset=queryset)
        queryset=myFilter.qs[:6]

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    # Return particular Quiz OR All quiz of request user
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


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    def create(self, request, *args, **kwargs):
        try:
            token=request.headers['authorization'][6:]
            userId = Token.objects.get(key=token).user.id
            rating=request.data['value']
            if int(rating) < 1 or 5 < int(rating):
                response = {'message': 'Wrong Rating'}
                return Response(response, status=status.HTTP_403_FORBIDDEN)
            Rating.objects.filter(user=userId).update(value=rating)
            response = {'message': 'Ok'}
            return Response(response, status=status.HTTP_200_OK)
        except:
            response = {'message': 'Something went wrong'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    
    def list(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use GET method like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use DELETE method like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use PUT method like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, *args, **kwargs):
        response = {'message': 'You can\'t use GET method like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class EntertainmentViewSet(viewsets.ModelViewSet):
    queryset = Entertainment.objects.all()
    serializer_class = EntertainmentSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        myFilter = EntertainmentFilter(request.GET,queryset=queryset)
        queryset=myFilter.qs

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class EntertainmentResultViewSet(viewsets.ModelViewSet):
    queryset = EntertainmentResult.objects.all()
    serializer_class = EntertainmentResultSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print(request.GET['category'])
        myFilter = EntertainmentResultFilter(request.GET,queryset=queryset)
        queryset=myFilter.qs
        if len(queryset)==0:
            cat = request.GET['category']
            code = int(request.GET['code'])//1000
            queryset=EntertainmentResult.objects.filter(category=cat).order_by('?')[:1]

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


