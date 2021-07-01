from django.urls import path, include
from rest_framework import routers
from . import views

# defining the simple router
router = routers.DefaultRouter()
router.register(r'', views.CategoryViewSet)
urlpatterns = [
    path('', include(router.urls))
]
