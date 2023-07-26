from django.urls import path

from task.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    TagUpdateView,
    TagDeleteView, index)

urlpatterns = [
    path("", index, name="index"),
    path("tags", TagListView.as_view(), name="tags"),
    path(
        "task/create",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "task/<int:pk>/update",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/<int:pk>/delete",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tag/<int:pk>/update",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tag/<int:pk>/delete",
        TagDeleteView.as_view(),
        name="tag-delete"
    )
]

app_name = "task"
