# Generated by Django 4.2.7 on 2023-11-14 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('secondary', '0004_remove_user_info_gender_alter_userinfo_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catgory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='分类名称')),
                ('desc', models.TextField(blank=True, default='', max_length=255, null=True, verbose_name='分类描述')),
                ('add_data', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='文章标签')),
                ('add_data', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('pub_data', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=61, verbose_name='文章标题')),
                ('desc', models.TextField(blank=True, default='', max_length=200, verbose_name='文章描述')),
                ('content', models.TextField(blank=True, null=True, verbose_name='文章标题')),
                ('add_data', models.DateTimeField(verbose_name='添加时间')),
                ('pub_data', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('catgory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.catgory', verbose_name='文章标签')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondary.user_info', verbose_name='作者')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tag', verbose_name='文章详情')),
            ],
        ),
    ]
