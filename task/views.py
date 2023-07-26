from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from task.forms import TaskForm, TagForm
from task.models import Task, Tag


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    tags = Tag.objects.all()


    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        try:
            task = Task.objects.get(pk=task_id)
            task.is_done = not task.is_done
            task.save()
            return HttpResponseRedirect(request.path_info)
        except Task.DoesNotExist:
            pass
    return render(request, "task/index.html", {"tasks": tasks, "tags": tags})


class TaskListView(generic.ListView):
    model = Task
    contest_object_name = "task-list"
    template_name = "task/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form = TaskForm
    fields = "__all__"
    success_url = reverse_lazy("task:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form = TaskForm
    fields = "__all__"
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:index")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "task/tags.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form = TagForm
    fields = "__all__"
    template_name = "task/tag_form.html"
    success_url = reverse_lazy("tag:list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form = TagForm
    fields = "__all__"
    success_url = reverse_lazy("task:tags")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tags")
