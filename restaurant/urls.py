#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='home'),
    path('about/', views.about, name="about"),
    path('api-menu/', views.MenuItemView.as_view(), name='api-menu'),
    path('api-menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
