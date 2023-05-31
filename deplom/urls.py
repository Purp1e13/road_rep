from django.contrib import admin
from django.urls import path
from deplom import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('info/', views.info, name='info'),
    path('login/', views.success, name='login'),
    path('test/', views.test, name='test'),
    path('admin/', admin.site.urls),
]
