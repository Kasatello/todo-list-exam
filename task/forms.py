from django import forms

from task.models import Task


class TaskForm(forms.ModelForm):
    tags = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = "__all__"
