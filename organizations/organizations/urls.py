from django.urls import include, path
from rest_framework import routers
from django.contrib import admin


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]