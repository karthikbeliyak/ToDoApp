from django import forms
from .models import Taskinfo

repeat_choices=[('Yes','Yes'),
         ('No','No')]

status_choices = [('New','New'),
        ('Working on this','In Progress'),
        ('Completed','Completed'),]


class TaskForm(forms.ModelForm):
    task_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    task_category = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    start_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=forms.TextInput(attrs={'class': 'form-control datetimepicker-input','data-target': '#datetimepicker1'}))
    end_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=forms.TextInput(attrs={'class': 'form-control datetimepicker-input','data-target': '#datetimepicker2'}))
    task_repeatative = forms.ChoiceField(choices=repeat_choices, widget=forms.RadioSelect)
    task_status = forms.ChoiceField(choices=status_choices, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Taskinfo
        fields = "__all__"