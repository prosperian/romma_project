from datetime import datetime, timedelta
from rest_framework import generics, status
from rest_framework.response import Response
from romma.serializers import BuySerializer, UserSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import Buy
from django.shortcuts import get_object_or_404


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request, ):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"Token ": user.auth_token.key})
        else:
            return Response({"Error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class Bought(APIView):

    def put(self, request):
        created_by = request.user
        buy = Buy.objects.get(created_by=created_by)
        buy.month_plan = True
        buy.started_at = datetime.now()
        buy.end_at = datetime.now() + timedelta(days=30)
        buy.save(update_fields=['month_plan', 'started_at', 'end_at'])
        return Response({'updated'})

    def post(self, request):
        created_by = request.user.id
        data = {'created_by': created_by}
        try:
            buy = Buy.objects.get(created_by=created_by)
            return Response({"User already exist"})
        except Buy.DoesNotExist:
            serializer = BuySerializer(data=data)
            if serializer.is_valid():
                buy = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        created_by = request.user.id
        buy = get_object_or_404(Buy, created_by=created_by)

        if buy.end_at.date() < datetime.now().date():
            buy.month_plan = False
            buy.save()

        data = {
            'created_by': created_by, 'started_at': buy.started_at, 'end_at': buy.end_at, 'month_plan': buy.month_plan
        }

        return Response(data, status=status.HTTP_200_OK)
