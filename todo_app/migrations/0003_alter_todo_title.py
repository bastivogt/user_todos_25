# Generated by Django 5.1.6 on 2025-02-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_app", "0002_alter_todo_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="title",
            field=models.CharField(max_length=150, verbose_name="title"),
        ),
    ]
