# Generated by Django 4.2.16 on 2025-02-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("b13project", "0009_remove_uploadedfile_author_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="location",
            field=models.CharField(default="USA", max_length=255),
            preserve_default=False,
        ),
    ]
