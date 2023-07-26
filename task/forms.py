from django import forms

from task.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = "__all__"


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = "__all__"
