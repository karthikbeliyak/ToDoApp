from django.db import models


# Create your models here.
class Taskinfo(models.Model):
    task_name = models.CharField(max_length = 100)
    task_category = models.CharField(max_length = 100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    repeat_choices=[('Yes','Yes'),
         ('No','No')]
    task_repeatative = models.CharField(max_length = 100, choices=repeat_choices)
    status_choices = [('New','New'),
        ('Working on this','In Progress'),
        ('Completed','Completed'),]
    task_status = models.CharField(max_length = 100)
