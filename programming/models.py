from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название курса')
    mentor = models.CharField(max_length=30, verbose_name='Имя Ментора')
    months = models.IntegerField(default=6, verbose_name='Длительность курсов')

    def __repr__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО Студента')
    laptop = models.CharField(max_length=20, choices=(
        ('mac', 'Macbook'),
        ('linux', 'Linux'),
        ('windows', 'Windows')
    ), verbose_name='Операционная система')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __repr__(self):
        return self.name

