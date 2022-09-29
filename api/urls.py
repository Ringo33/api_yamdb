from django.urls import path

from api import views

urlpatterns = [
    path('auth/email/', views.send_email, name='send_email'),
]