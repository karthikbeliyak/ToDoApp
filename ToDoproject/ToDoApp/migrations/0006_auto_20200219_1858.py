# Generated by Django 2.2.3 on 2020-02-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0005_auto_20200219_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskinfo',
            name='repeatative_task',
            field=models.CharField(max_length=100),
        ),
    ]
