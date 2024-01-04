from django.urls import path
from modelsales.apps import ModelsalesConfig
from rest_framework.routers import DefaultRouter

from modelsales.views import ModelsalesViewSet

router = DefaultRouter()
router.register(r'modelsales', ModelsalesViewSet, basename='modelsales')

app_name = ModelsalesConfig.name

urlpatterns = [

] + router.urls