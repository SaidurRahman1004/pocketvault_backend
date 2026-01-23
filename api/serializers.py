from rest_framework import serializers
from .models import ShoppingItem, MediaItem, Bookmark
from django.contrib.auth.models import User
#User Serializer For User Registration And Info
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        #Create User With hash paswod
    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            email= validated_data.get('email', ""),
            password= validated_data['password']
        )
        return user
#ShoppingItem Serializer
class ShoppingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItem
        fields = ['id', 'user', 'name', 'category', 'isBought']
        read_only_fields = ['user'] #User Field Is Read-Only

#Bookmark Serializer
class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'user', 'title', 'url', 'category']
        read_only_fields = ['user'] #User Field Is Read-Only
#MediaItem Serializer
class MediaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaItem
        fields = ['id', 'user', 'title', 'type', 'status', 'rating', 'review']
        read_only_fields = ['user'] #User Field Is Read-Only