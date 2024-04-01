# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from .views import (
    UsersListApiView,
)

urlpatterns = [
    path('users', UsersListApiView.as_view(), name="users"),
]