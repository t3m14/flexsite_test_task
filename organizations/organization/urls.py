from django.urls import path
from organization.views import OrganizationViewSet, CreateOrganizationView

urlpatterns = [
    path('', OrganizationViewSet.as_view({'get': 'list'})),
    path('create/', CreateOrganizationView.as_view()),
    
]