from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Course, Student
from .forms import CourseForm, StudentForm
from django.views import View
from  django.views import generic

def course_list(request):
    courses = Course.objects.all()
    context = {
        'courses':courses
    }
    return render(request, 'course_list.html', context)

def course_create(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('course_list'))
    context={
        'form':form
    }
    return render(request, 'course_form.html', context)


def course_detail(request, id):
    course = Course.objects.get(id=id)
    context={
         'course':course
    }
    return render(request, 'course_detail.html', context)

def course_update(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm(instance=course)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect(course.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'course_form.html', context)

def course_delete(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        course.delete()
        return redirect(reverse_lazy('course_list'))
    context = {
        'course': course
    }
    return render(request, 'course_delete.html', context)


# class StudentListView(View):
#     def get(self, request, *args, **kwargs):
#         students = Student.objects.all()
#         context = {
#             'students': students
#         }
#         return render(request, 'student_list.html', context)

class StudentListView(generic.ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

# class StudentCreateView(View):
#     def get(self, request, *args, **kwargs):
#         form = StudentForm()
#         context = {
#             'form': form
#         }
#         return render(request, 'student_form.html', context)

class StudentCreateView(generic.CreateView):
    model = Student
    # fields = '__all__'
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')


class StudenyDetailView(generic.DetailView):
    model = Student
    # context_object_name = 'student'
    template_name = 'student_detail.html'
    # pk_url_kwarg = 'id'

class StudentUpdateView(generic.UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    context_object_name = 'student'

class StudentDeleteView(generic.DeleteView):
    model = Student
    template_name = 'student_delete.html'
    context_object_name = 'student'
    success_url = reverse_lazy('student_list')





