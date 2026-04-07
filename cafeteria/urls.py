from django.contrib import admin
from django.urls import path, include
import django_cas_ng.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login', django_cas_ng.views.LoginView.as_view(), name='cas_ng_login'),
    path('accounts/logout', django_cas_ng.views.LogoutView.as_view(), name='cas_ng_logout'),
    path('', include(('cafeteria_app.urls', 'cafeteria_app'), namespace='cafeteria_app')),
]
