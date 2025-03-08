from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'priority', 'due_datetime', 'completed']  # ✅ เพิ่ม due_datetime
        widgets = {
            'priority': forms.Select(choices=Task.PRIORITY_CHOICES, attrs={'class': 'form-select'}),
            'due_datetime': forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}),  # ✅ DateTime Picker
        }