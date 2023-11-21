# Generated by Django 4.2.7 on 2023-11-20 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_user_post_delete_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_post',
            name='add_data',
        ),
        migrations.RemoveField(
            model_name='user_post',
            name='pub_data',
        ),
        migrations.AlterField(
            model_name='user_post',
            name='catgory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.catgory', verbose_name='文章分类'),
        ),
    ]