from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views
from api.views import UserViewSet, UsernameViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'users', UsernameViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/email/', views.send_email, name='send_email'),
    path('auth/token/', views.send_token, name='send_token'),
    # path('users/', UserViewSet.as_view({'get': 'list'}), name='user_view_set'),
]