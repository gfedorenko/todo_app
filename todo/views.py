from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from .forms import UserRegistrationForm
from .models import Task


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


@method_decorator(login_required, name="dispatch")
class TaskListView(View):
    model = View

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(user=request.user).order_by("-id")
        context = {"tasks": tasks}

        return render(request, "todo.html", context)

    def post(self, request, *args, **kwargs):

        task_name = request.POST.get("new-task")
        task_desc = request.POST.get("new-task-desc")

        todo = Task.objects.create(name=task_name, desc=task_desc, user=request.user)
        return redirect("home")


@method_decorator(login_required, name="dispatch")
class TaskView(View):
    model = View

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs["pk"])
        context = {"tasks": [task]}

        return render(request, "todo.html", context)

    # def post(self, request, *args, **kwargs):
    #     task_name = request.POST.get("new-task")
    #     task_desc = request.POST.get("new-task-desc")

    #     task = Task.objects.create(name=task_name, desc=task_desc, user=request.user)
    #     return redirect("home")

    # def put(self, request, *args, **kwargs):
    #     task_name = request.get("new-task")
    #     task_desc = request.get("new-task-desc")

    #     task = get_object_or_404(Task, id=kwargs["pk"], user=request.user)

    #     task = Task.objects.create(name=task_name, desc=task_desc, user=request.user)
    #     return redirect("home")

    def delete(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs["pk"], user=request.user)
        task.delete()
        tasks = Task.objects.filter(user=request.user).order_by("-id")
        context = {"tasks": tasks}

        if request.htmx:
            base_template = "partials/_tasks.html"
        else:
            base_template = "todo.html"

        return render(request, base_template, context)
