# Generated by Django 5.0 on 2023-12-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("file", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="filemodel",
            name="mimetypes",
        ),
        migrations.RemoveField(
            model_name="filemodel",
            name="size",
        ),
        migrations.RemoveField(
            model_name="filemodel",
            name="uploaded_at",
        ),
        migrations.AlterField(
            model_name="filemodel",
            name="name",
            field=models.CharField(max_length=1024),
        ),
    ]
