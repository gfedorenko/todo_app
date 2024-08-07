from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.http import QueryDict

from .forms import UserRegistrationForm
from .models import Task


@method_decorator(login_required, name="dispatch")
class TaskListView(View):
    model = View

    def get(self, request, *args, **kwargs):
        order = request.GET.get("order")

        if order:
            tasks = tasks = Task.objects.filter(user=request.user).order_by(
                "is_completed",
                "-priority",
            )
        else:
            tasks = Task.objects.filter(user=request.user)
        context = {"tasks": tasks}

        if request.htmx:
            base_template = "partials/_tasks.html"
        else:
            base_template = "todo.html"

        return render(request, base_template, context)

    def post(self, request, *args, **kwargs):

        task_name = request.POST.get("name")
        task_desc = request.POST.get("desc")
        task_priority = request.POST.get("priority")

        task = Task.objects.create(
            name=task_name, desc=task_desc, priority=task_priority, user=request.user
        )
        return redirect("home")


@method_decorator(login_required, name="dispatch")
class TaskView(View):
    model = View

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs["pk"])
        context = {"tasks": [task]}

        return render(request, "todo.html", context)

    def put(self, request, *args, **kwargs):
        data = QueryDict(request.body)

        task = get_object_or_404(Task, id=kwargs["pk"], user=request.user)

        task.name = data.get("name", task.name)
        task.desc = data.get("desc", task.desc)
        task.priority = data.get("priority", task.priority)

        task.save()

        tasks = Task.objects.filter(user=request.user)
        context = {"tasks": tasks}

        if request.htmx:
            base_template = "partials/_tasks.html"
        else:
            base_template = "todo.html"

        return render(request, base_template, context)

    def delete(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs["pk"], user=request.user)
        task.delete()
        tasks = Task.objects.filter(user=request.user)
        context = {"tasks": tasks}

        if request.htmx:
            base_template = "partials/_tasks.html"
        else:
            base_template = "todo.html"

        return render(request, base_template, context)


def complete_task(request, *args, **kwargs):
    task = get_object_or_404(Task, id=kwargs["pk"], user=request.user)
    task.is_completed = True
    task.save()

    tasks = Task.objects.filter(user=request.user)
    context = {"tasks": tasks}

    if request.htmx:
        base_template = "partials/_tasks.html"
    else:
        base_template = "todo.html"

    return render(request, base_template, context)


def register(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "register.html", context)
