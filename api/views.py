from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import User
from api.serializers import UsersSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def send_email(request):
    serializer = UsersSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data['email']
    username = serializer.data['username']
    user, created = User.objects.get_or_create(email=email, username=username)
    conf_code = default_token_generator.make_token(user)
    send_mail(
        'Confirmation code from Yamdb',
        f'This is your confirmation code: {conf_code}',
        'from@example.com',
        [email],
        fail_silently=False
        )
    return Response('Your confirmation code has been sent by e-mail')


# class RegisterView(APIView):
#     permission_classes = (AllowAny,)
#
#     def post(self, request):
#         serializer = UsersSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         email = serializer.data['email']
#         username = serializer.data['username']
#         user, created = User.objects.get_or_create(
#             email=email,
#             username=username
#         )
#         conf_code = default_token_generator.make_token(user)
#         send_mail_to_user()
#





