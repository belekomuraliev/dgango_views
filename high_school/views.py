from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import TeacherForm, PupilForm
from .models import Teacher, Pupil
from  django.views import generic


def teacher_list(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers':teachers
    }
    return render(request, 'teacher_list.html', context)

def teacher_create(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('teacher_list'))
    context = {
        'form':form
    }
    return render(request, 'teacher_form.html', context)

def teacher_detail(request, id):
    teacher = Teacher.objects.get(id=id)
    context = {
        'teacher':teacher
    }
    return render(request, 'teacher_detail.html', context)

def teacher_update(request, id):
    teacher = Teacher.objects.get(id=id)
    form = TeacherForm(instance=teacher)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('teacher_list'))
    context = {
        'form': form
    }
    return render(request, 'teacher_form.html', context)

def teacher_delete(request,id):
    teacher = Teacher.objects.get(id=id)
    if request.method == 'POST':
        teacher.delete()
        return redirect(reverse_lazy('teacher_list'))
    context = {
        'teacher': teacher
    }
    return render(request, 'teacher_delete.html', context)


class PupilListView(generic.ListView):
    model = Pupil
    template_name = 'pupil_list.html'
    context_object_name = 'pupils'

class PupilCreateView(generic.CreateView):
    model = Pupil
    form_class = PupilForm
    template_name = 'pupil_form.html'
    success_url = reverse_lazy('pupil_list')

class PupilDetailView(generic.DetailView):
    model = Pupil
    template_name = 'pupil_detail.html'

class PupilUpdateView(generic.UpdateView):
    model = Pupil
    form_class = PupilForm
    template_name = 'pupil_form.html'
    context_object_name = 'pupil'
    success_url = reverse_lazy('pupil_list')

class PupilDeleteView(generic.DeleteView):
    model = Pupil
    template_name = 'pupil_delete.html'
    context_object_name = 'pupil'
    success_url = reverse_lazy('pupil_list')




