# Generated by Django 4.2.7 on 2023-11-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0010_suggestion"),
    ]

    operations = [
        migrations.AddField(
            model_name="suggestion",
            name="su_title",
            field=models.CharField(default=" ", max_length=32, verbose_name="建议标题"),
        ),
    ]
