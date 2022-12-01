
from django.urls import path
from . import views
urlpatterns = [
    path('teacher/', views.teacher_list, name='teacher_list'),
    path('teacher_create/', views.teacher_create, name='teacher_create'),
]
