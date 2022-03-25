from rest_framework import serializers

from .models import Person
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Person
        fields = ['user', 'email', 'gender','first_name','last_name']

class OnlyPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"