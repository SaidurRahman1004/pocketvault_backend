from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    #api auth All Endpoints
    path('api/', include('api.urls')),
    #login urls for obtaining and refreshing JWT tokens
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #new token Url if the old one is expired
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #Default Auth Login/Logout Views
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
