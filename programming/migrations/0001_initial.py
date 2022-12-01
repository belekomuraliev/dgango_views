# Generated by Django 3.2 on 2022-12-01 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название курса')),
                ('mentor', models.CharField(max_length=30, verbose_name='Имя Ментора')),
                ('months', models.IntegerField(default=6, verbose_name='Длительность курсов')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='ФИО Студента')),
                ('laptop', models.CharField(choices=[('mac', 'Macbook'), ('linux', 'Linux'), ('windows', 'Windows')], max_length=20, verbose_name='Операционная система')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programming.course')),
            ],
        ),
    ]