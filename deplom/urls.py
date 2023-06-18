from django.contrib import admin
from django.urls import path
from deplom import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('info/', views.info, name='info'),
    path('news/', views.news, name='news'),
    path('work/', views.work, name='work'),
    path('workphoto1/', views.workphoto1, name='workphoto1'),
    path('workphoto2/', views.workphoto2, name='workphoto2'),
    path('login/', views.login_user, name='login'),
    path('tasks/', views.tasks, name='tasks'),
    path('logout/', views.logout_user, name='logout'),
    path('test/', views.test, name='test'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)