from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('cafeteria_app.urls', 'cafeteria_app'), namespace='cafeteria_app')),
]