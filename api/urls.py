from .views import ShoppingItemViewSet, MediaItemViewSet, BookmarkViewSet, UserCreate
from rest_framework.routers import DefaultRouter
from django.urls import path, include
#API Router Setup
#r mean raw string to avoid escape character issues
router = DefaultRouter()
router.register(r'users', UserCreate, basename='user')
router.register(r'shopping-items', ShoppingItemViewSet, basename='shoppingitem')
router.register(r'bookmarks', BookmarkViewSet,basename='bookmark')
router.register(r'media-items', MediaItemViewSet, basename='mediaitem')

urlpatterns = [
    path('', include(router.urls)),
]
