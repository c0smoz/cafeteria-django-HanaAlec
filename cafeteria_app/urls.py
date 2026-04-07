from django.urls import path
from . import views
from django_cas_ng import views as cas_views

app_name = 'cafeteria_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('users/', views.user_list, name='user_list'),
    path('users/add/', views.user_add, name='user_add'),
    path('users/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),
    # path('accounts/login/', cas_views.login, name='cas_ng_login'),
    # path('accounts/logout/', cas_views.logout, name='cas_ng_logout'),
]
