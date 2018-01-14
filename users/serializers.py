from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserListSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class UserSerializer(UserListSerializer):

    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_username(self, data):
        if self.instance is None and User.objects.filter(username=data).exists():
            raise ValidationError("Use already exists")
        if self.instance and self.instance.username != data and User.objects.filter(username=data).exists():
            raise ValidationError("Wanted username is already in use")
        return data

    def create(self, validated_data):
        instance = User()
        return self.update(instance,validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.username = validated_data.get("username")
        instance.email = validated_data.get("email")
        instance.set_password(validated_data.get("password"))
        instance.save()
        return instance



class BlogSerializer(serializers.ModelSerializer):

    user_url = serializers.SerializerMethodField('is_user_URL')

    def is_user_URL(self, obj):
        return "http://127.0.0.1:8000/api/1.0/posts/" + obj.username
    class Meta:
        model = User

        fields = ["username", "first_name", "last_name", "user_url"]