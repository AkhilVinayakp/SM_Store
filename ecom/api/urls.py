from django.urls import path, include
# TODO
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path("", home, name="api.home"),
    # adding the category path with it's own urls
    path("category/", include('api.category.urls')),
]
