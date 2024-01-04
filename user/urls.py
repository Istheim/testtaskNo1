from django.urls import path
from rest_framework.routers import DefaultRouter

from user.apps import UserConfig
from user.views import UsersViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UserConfig.name

router = DefaultRouter()
router.register(r'user', UsersViewSet, basename='user')

urlpatterns = [
                  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + router.urls