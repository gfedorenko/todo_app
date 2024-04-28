from django.test import TestCase

from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test_user")
        self.task = Task.objects.create(
            name="Test Task", desc="This is a test task", user=self.user
        )

    def test_task_creation(self):
        self.assertEqual(self.task.name, "Test Task")
        self.assertEqual(self.task.desc, "This is a test task")
        self.assertFalse(self.task.is_completed)
        self.assertEqual(self.task.priority, Task.TaskPriority.NORMAL)
        self.assertEqual(self.task.user, self.user)


class TaskViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="password")
        self.client = Client()
        self.client.login(username="test_user", password="password")
        self.task = Task.objects.create(
            name="Test Task", desc="This is a test task", user=self.user
        )

    def test_task_list_view_get(self):
        response = self.client.get(reverse("tasks"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_task_list_view_post(self):
        response = self.client.post(
            reverse("tasks"),
            {
                "name": "New Task",
                "desc": "Description for new task",
                "priority": Task.TaskPriority.NORMAL,
            },
        )
        self.assertEqual(response.status_code, 302)

    def test_task_detail_view_get(self):
        response = self.client.get(reverse("task", args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_task_detail_view_put(self):
        data = {
            "name": "Updated Task",
            "desc": "Updated description for task",
            "priority": Task.TaskPriority.HIGH,
        }

        response = self.client.put(
            reverse("task", args=[self.task.id]),
            data=data,
            content_type="application/x-www-form-urlencode",
        )

        self.assertEqual(response.status_code, 200)

    def test_task_detail_view_delete(self):
        response = self.client.delete(reverse("task", args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
