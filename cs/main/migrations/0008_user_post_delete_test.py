# Generated by Django 4.2.7 on 2023-11-20 04:54

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):
    dependencies = [
        ("secondary", "0005_alter_user_info_name"),
        ("main", "0007_alter_test_content"),
    ]

    operations = [
        migrations.CreateModel(
            name="User_Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=32, verbose_name="文章标题")),
                ("content", mdeditor.fields.MDTextField(verbose_name="具体内容")),
                ("add_data", models.DateTimeField(verbose_name="添加时间")),
                ("pub_data", models.DateTimeField(auto_now=True, verbose_name="修改时间")),
                (
                    "catgory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.catgory",
                        verbose_name="文章标签",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="secondary.user_info",
                        verbose_name="作者",
                    ),
                ),
                (
                    "tags",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.tag",
                        verbose_name="文章标签",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="test",
        ),
    ]
