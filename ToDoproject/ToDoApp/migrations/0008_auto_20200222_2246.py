# Generated by Django 2.2.3 on 2020-02-22 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0007_auto_20200222_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskinfo',
            name='task_status',
            field=models.CharField(max_length=100),
        ),
    ]