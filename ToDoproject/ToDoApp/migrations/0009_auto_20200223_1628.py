# Generated by Django 2.2.3 on 2020-02-23 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0008_auto_20200222_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskinfo',
            name='task_status',
            field=models.CharField(default='Select here', max_length=100),
        ),
    ]
