from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken
from api.models import User
from api.permissions import IsAuthorOrReadOnly
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


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['POST'])
@permission_classes([AllowAny,])
def send_token(request):
    serializer = UsersSerializer(data=request.data)
    serializer.is_valid(raise_exception=False)
    email = serializer.data['email']
    user = get_object_or_404(User, email=email)
    conf_code = serializer.data['conf_code']
    check_token = default_token_generator.check_token(user, conf_code)
    if check_token:
        token = get_tokens_for_user(user)
        return Response(token)
    return Response('Вы направили некорректный confirmation_code.'
                    ' Просьба проверить и направить корректные данные.')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAdminUser,
                          ]
    lookup_field = 'username'

    def perform_create(self, serializer):
        first_name = self.request.data.get('first_name')
        last_name = self.request.data.get('last_name')
        username = self.request.data.get('username')
        email = self.request.data.get('email')
        role = self.request.data.get('role')
        User.objects.create_user(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            role = role
        )


    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            user_search = get_object_or_404(User, username=search)
            queryset = User.objects.filter(id=user_search.id)
            return queryset
        return User.objects.all()


# class UsernameViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UsersSerializer
#     permission_classes = [permissions.IsAdminUser,
#                           ]
#     lookup_field = 'username'
#
#     def get_queryset(self):
#         username = self.kwargs.get('username')
#         print(username)
#         # if search:
#         #     user_search = get_object_or_404(User, username=search)
#         #     queryset = User.objects.filter(id=user_search.id)
#         #     return queryset
#         return User.objects.all()