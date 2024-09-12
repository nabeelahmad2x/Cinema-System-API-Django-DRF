from django.contrib.auth import authenticate
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from django.contrib.auth import authenticate, login
from django.contrib.sessions.models import Session


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)

            request.session['username'] = username
            request.session.save()
            return Response(f'Logged in. Session Key:{request.session.session_key}', status=status.HTTP_200_OK)
        else:
            return Response('Invalid email or password', status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):

    def post(self, request):
        request.session.delete()
        return Response({"Logout OK."}, status=status.HTTP_200_OK)
