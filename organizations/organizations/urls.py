from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from user.urls import urlpatterns as user_urls
from organization.urls import urlpatterns as organization_urls
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.DefaultRouter()

urlpatterns = [
    path('user/', include(user_urls)),
    path('organization/', include(organization_urls)),
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'), 
    path('admin/', admin.site.urls),
]