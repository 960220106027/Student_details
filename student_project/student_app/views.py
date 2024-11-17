from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Subject
from .forms import StudentForm, SubjectForm



def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})
def student_list(request):
    query = request.GET.get('search', '')
    students = Student.objects.filter(name__icontains=query) if query else Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_detail.html', {'student': student})

def add_subject(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.student = student
            subject.save()
            return redirect('student_detail', pk=student.id)
    else:
        form = SubjectForm()
    return render(request, 'subject_form.html', {'form': form, 'student': student})
