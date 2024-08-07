from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from .views import register, complete_task, TaskListView, TaskView

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/", TaskListView.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskView.as_view(), name="task"),
    path("task/<int:pk>/complete", complete_task, name="complete_task"),
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="login.html"), name="logout"),
]
