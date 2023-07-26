from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=355)
    creation_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ["is_done", "-creation_date"]

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
