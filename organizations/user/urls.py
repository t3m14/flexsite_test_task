
from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'api'

urlpatterns = [
    path('register/',views.RegisterView.as_view(),name="register"),
    path('login/',views.LoginAPIView.as_view(),name="login"),
    path('logout/', views.LogoutAPIView.as_view(), name="logout"),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.EditUserProfileView.as_view(), name='edit_profile'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    ]