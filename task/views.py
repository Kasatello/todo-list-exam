from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from task.models import Task, Tag


def index(request: HttpRequest) -> HttpResponse:

    return render(request, "task/index.html")


class TaskListView(generic.View):
    model = Task
    contest_object_name = "index"
    template_name = "task/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:home")


class TagListView(generic.View):
    model = Tag
    template_name = "task/tags.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tags")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tags")
