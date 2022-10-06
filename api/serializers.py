from rest_framework import serializers
from api.models import User

CHOICES = [
    ('user', 'user'),
    ('admin', 'admin'),
    ('moderator', 'moderator'),
]

class UsersSerializer(serializers.ModelSerializer):
    # password = serializers.ReadOnlyField(source='user.password')
    # last_login = serializers.ReadOnlyField(source='user.last_login')
    # role = serializers.ChoiceField(default='user', choices=CHOICES)
    class Meta:
        fields = ['first_name', 'last_name', 'username', 'email', 'role']
        model = User
