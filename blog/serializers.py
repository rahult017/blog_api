from rest_framework import serializers
from .models import Blog
from django.contrib.auth import get_user_model

User = get_user_model()

def validate_only_characters(value, field_name):
    if not value.isalpha():
        raise serializers.ValidationError(f'Only characters are allowed in the {field_name} field.')
    

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
    class Meta:
        model = User
        fields = ['id', 'user', 'password']
    
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        
    def validate_title(self, value):
        validate_only_characters(value, 'title')
        return value
