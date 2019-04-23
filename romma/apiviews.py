from datetime import datetime, timedelta

from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from romma.serializers import BuySerializer, UserSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import Buy
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from rest_framework.permissions import AllowAny


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class ResetPassword(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get("email")
        try:
            user = User.objects.get(email=email)
            password = User.objects.make_random_password()
            user.set_password(password)
            message = ' .تغییر یافت ' + password + ' رمز عبور شما به '
            send_mail(
                'رُما، تغییر رمز عبور',
                message,
                'rommaforgetpass@gmail.com',
                [email],
                fail_silently=False,
            )
            user.save()
            return Response({"password changed"})
        except User.DoesNotExist:
            return Response({"no user with this email"})


class LoginView(APIView):
    permission_classes = ()

    def post(self, request, ):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user:
            return Response({"Token ": user.auth_token.key})
        else:
            return Response({"Error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class Bought(APIView):

    def put(self, request):
        created_by = request.user
        buy = Buy.objects.get(created_by=created_by)
        month_plan = request.data.get("month_plan")
        year_plan = request.data.get("year_plan")
        if month_plan:
            buy.month_plan = True
            buy.end_at = datetime.now() + timedelta(days=30)
        else:
            buy.month_plan = False
        if year_plan:
            buy.year_plan = True
            buy.end_at = datetime.now() + timedelta(days=365)
        else:
            buy.year_plan = False
        buy.started_at = datetime.now()
        buy.save(update_fields=['month_plan', 'year_plan', 'started_at', 'end_at'])
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
                month_plan = request.data.get("month_plan")
                year_plan = request.data.get("year_plan")
                buy = serializer.save()
                if month_plan:
                    buy.month_plan = True
                    buy.end_at = datetime.now() + timedelta(days=30)
                else:
                    buy.month_plan = False
                if year_plan:
                    buy.year_plan = True
                    buy.end_at = datetime.now() + timedelta(days=365)
                else:
                    buy.year_plan = False

                serializer.save()
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
            'created_by': created_by, 'started_at': buy.started_at, 'end_at': buy.end_at,
            'month_plan': buy.month_plan, 'year_plan': buy.year_plan
        }

        return Response(data, status=status.HTTP_200_OK)
