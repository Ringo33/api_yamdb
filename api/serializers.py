from rest_framework import serializers

from api.models import User


class UsersSerializer(serializers.ModelSerializer):
    # password = serializers.ReadOnlyField(source='user.password')
    # last_login = serializers.ReadOnlyField(source='user.last_login')
    class Meta:
        fields = '__all__'
        model = User