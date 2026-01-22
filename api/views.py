from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, ShoppingItemSerializer, BookmarkSerializer, MediaItemSerializer
from .models import ShoppingItem, Bookmark, MediaItem
#User ViewSet For User Registration And Info
class UserCreate(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to create  user

#ShoppingItem ViewSet
class ShoppingItemViewSet(viewsets.ModelViewSet):
    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    #Show only items that belong to the logged-in user //only login user Item shown
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    #when new item is created, set the current user(logged in user) automatically as the owner of the item 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



#Bookmark ViewSet
class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    #Show only items that belong to the logged-in user //only login user Item shown
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    #when new item is created, set the current user(logged in user) automatically as the owner of the item 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
#MediaItem ViewSet
class MediaItemViewSet(viewsets.ModelViewSet):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    #Show only items that belong to the logged-in user //only login user Item shown
    def get_queryset(self):
        return self.queryset.filter(user =self.request.user)
    #when new item is created, set the current user(logged in user) automatically as the owner of the item 
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)