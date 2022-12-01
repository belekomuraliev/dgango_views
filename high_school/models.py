from django.db import models



class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО учителя')
    class_name = models.CharField(max_length=20, choices=(
        ('a_class', 'A_class'),
         ('b_class', 'B_class'),
        ('c_class', 'C_class'),
    ), verbose_name= 'Название класса')

class Pupil(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО ученика')
    birth_date = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

