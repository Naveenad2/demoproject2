# Generated by Django 4.1.10 on 2024-01-26 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edit_Home_Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Main_heading', models.CharField(max_length=100)),
                ('Discription', models.TextField(max_length=700)),
                ('Main_photo', models.ImageField(upload_to='./static/images')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catogory_name', models.CharField(max_length=100)),
                ('catogory_discription', models.TextField(max_length=100)),
                ('catogory_photo', models.ImageField(upload_to='./static/images')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video_name', models.CharField(max_length=100)),
                ('Video_discription', models.TextField(max_length=500)),
                ('video_image', models.ImageField(upload_to='./static/images')),
                ('Choose_video', models.FileField(upload_to='./static/vedio')),
                ('Choose_catogory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.lecture_category')),
            ],
        ),
    ]
