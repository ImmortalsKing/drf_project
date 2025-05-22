from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.UsersListApiView)

urlpatterns = [
    path('list/', include(router.urls)),
    path('me/', views.UserDetailApiView.as_view()),
    path('register/', views.RegisterApiView.as_view())
]