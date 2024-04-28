from django.urls import path, include
from django.contrib.auth.views import LoginView

from .views import register, TaskListView, TaskView

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/", TaskListView.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskView.as_view(), name="task"),
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
]
