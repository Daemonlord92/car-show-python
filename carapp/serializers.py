from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Car, Owner


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user