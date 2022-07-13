import datetime
from django.shortcuts import redirect, render
from task_manager.forms import AddNoteForm, AddNoteForm2, AddProjectForm, AddTaskForm, UpdateNoteForm

from task_model_manager.models import Note, Project, Task

# Create your views here.


def home(request):
    tasks = Task.objects.all().order_by("start_date")
    notes = Note.objects.all()
    update_notes_form = UpdateNoteForm()

    context = {
        "tasks": tasks,
        "notes": notes,
        "project_count": Project.objects.all().count,
        "update_notes_form": update_notes_form,
        "add_project_form": AddProjectForm(),
        "add_task_form": AddTaskForm(),
        "add_note_form": AddNoteForm(),
        "add_note_form2": AddNoteForm2()
    }

    return render(request, 'task_manager/home.html', context)


def today(request):
    tasks = Task.objects.all().filter(start_date=datetime.date.today())
    notes = Note.objects.all()
    update_notes_form = UpdateNoteForm()

    context = {
        "tasks": tasks,
        "notes": notes,
        "project_count": Project.objects.all().count,
        "update_notes_form": update_notes_form,
        "add_project_form": AddProjectForm(),
        "add_task_form": AddTaskForm(),
        "add_note_form": AddNoteForm(),
        "add_note_form2": AddNoteForm2()
    }

    return render(request, 'task_manager/home.html', context)


def tomorrow(request):
    tasks = Task.objects.all().filter(
        start_date=datetime.date.today() + datetime.timedelta(days=1))
    notes = Note.objects.all()
    update_notes_form = UpdateNoteForm()

    context = {
        "tasks": tasks,
        "notes": notes,
        "project_count": Project.objects.all().count,
        "update_notes_form": update_notes_form,
        "add_project_form": AddProjectForm(),
        "add_task_form": AddTaskForm(),
        "add_note_form": AddNoteForm(),
        "add_note_form2": AddNoteForm2()
    }

    return render(request, 'task_manager/home.html', context)


def overdue(request):
    all_tasks = Task.objects.all()
    tasks = []

    for task in all_tasks:
        if task.end_date < datetime.date.today() and not task.status:
            tasks.append(task)

    notes = Note.objects.all()
    update_notes_form = UpdateNoteForm()

    context = {
        "tasks": tasks,
        "notes": notes,
        "project_count": Project.objects.all().count,
        "update_notes_form": update_notes_form,
        "add_project_form": AddProjectForm(),
        "add_task_form": AddTaskForm(),
        "add_note_form": AddNoteForm(),
        "add_note_form2": AddNoteForm2()
    }

    return render(request, 'task_manager/home.html', context)


def project(request):
    projects = Project.objects.all()
    notes = Note.objects.all()
    update_notes_form = UpdateNoteForm()

    done_tasks = 0

    for project in projects:
        tasks = Task.objects.all().filter(project=project)
        for task in tasks:
            if task.status:
                done_tasks += 1

    context = {
        "projects": projects,
        "notes": notes,
        "task_count": Task.objects.all().count,
        "update_notes_form": update_notes_form,
        "done_tasks": done_tasks,
        "add_project_form": AddProjectForm(),
        "add_task_form": AddTaskForm(),
        "add_note_form": AddNoteForm(),
        "add_note_form2": AddNoteForm2()
    }

    return render(request, 'task_manager/home.html', context)


def project_tasks(request, id):
    tasks = Project.objects.get(id=id).tasks.all
    notes = Note.objects.all()
    update_notes_form = UpdateNoteForm()

    context = {
        "tasks": tasks,
        "notes": notes,
        "project_count": Project.objects.all().count,
        "update_notes_form": update_notes_form,
        "add_project_form": AddProjectForm(),
        "add_task_form": AddTaskForm(),
        "add_note_form": AddNoteForm(),
        "add_note_form2": AddNoteForm2()
    }

    return render(request, 'task_manager/home.html', context)


def search(request):
    if request.method == "GET":
        search = request.GET.get('search')
        tasks = Task.objects.filter(task__contains=search)
        notes = Note.objects.all()
        update_notes_form = UpdateNoteForm()
        projects = Project.objects.filter(project__contains=search)

        done_tasks = 0

        for project in projects:
            p_tasks = Task.objects.all().filter(project=project)
            for p_task in p_tasks:
                if p_task.status:
                    done_tasks += 1

        context = {
            "tasks": tasks,
            "notes": notes,
            "projects": projects,
            "update_notes_form": update_notes_form,
            "done_tasks": done_tasks,
            "add_project_form": AddProjectForm(),
            "add_task_form": AddTaskForm(),
            "add_note_form": AddNoteForm(),
            "add_note_form2": AddNoteForm2()
        }

        return render(request, 'task_manager/home.html', context)
    else:
        pass


def notes(request, id):
    tasks = Task.objects.all().filter(id=id)
    notes = Task.objects.get(id=id).notes.all
    update_notes_form = UpdateNoteForm()
    selected_task = Task.objects.get(id=id)

    context = {
        "tasks": tasks,
        "notes": notes,
        "selected_task": selected_task,
        "project_count": Project.objects.all().count,
        "update_notes_form": update_notes_form,
        "add_project_form": AddProjectForm(),
        "add_task_form": AddTaskForm(),
        "add_note_form": AddNoteForm(),
        "add_note_form2": AddNoteForm2()
    }

    return render(request, 'task_manager/home.html', context)


def update_notes(request, id):
    if request.method == "POST":
        update_notes_form = UpdateNoteForm(
            request.POST, instance=Note.objects.get(id=id))
        if update_notes_form.is_valid():
            update_notes_form.save()
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        return redirect(request.META.get('HTTP_REFERER'))


def update_task(request, id):
    task = Task.objects.get(id=id)
    task.status = not task.status
    task.save()

    return redirect(request.META.get('HTTP_REFERER'))


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def add_project(request):
    if request.method == "POST":
        add_project_form = AddProjectForm(request.POST)
        if add_project_form.is_valid():
            add_project_form.save()
            return redirect('projects')

    else:
        add_project_form = AddProjectForm()

    return redirect(request.META.get('HTTP_REFERER'))

def add_task(request):
    if request.method == "POST":
        add_task_form = AddTaskForm(request.POST)
        if add_task_form.is_valid():
            add_task_form.save()
            return redirect('home')

    else:
        add_task_form = AddTaskForm()

    return redirect(request.META.get('HTTP_REFERER'))

def add_task2(request, id):
    if request.method == "POST":
        add_task_form = AddTaskForm(request.POST)
        if add_task_form.is_valid():
            a_t_f = add_task_form.save(commit=False)
            a_t_f.project = Project.objects.get(id=id)
            a_t_f.save()
            return redirect('project_tasks', id)

    else:
        add_task_form = AddTaskForm()

    return redirect(request.META.get('HTTP_REFERER'))

def add_note(request):
    if request.method == "POST":
        add_note_form = AddNoteForm(request.POST)
        if add_note_form.is_valid():
            add_note_form.save()
            return redirect('home')

    else:
        add_note_form = AddNoteForm()

    return redirect(request.META.get('HTTP_REFERER'))

def add_note2(request, id):
    if request.method == "POST":
        add_note_form2 = AddNoteForm2(request.POST)
        if add_note_form2.is_valid():
            note = add_note_form2.save(commit=False)
            note.task = Task.objects.get(id=id)
            note.save()
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        add_note_form2 = AddNoteForm2()

    return redirect(request.META.get('HTTP_REFERER'))


def edit_project(request, id):
    if request.method == "POST":
        add_project_form = AddProjectForm(request.POST or None, instance=Project.objects.get(id=id))
        if add_project_form.is_valid():
            add_project_form.save()
            return redirect('projects')

    else:
        add_project_form = AddProjectForm(instance=Project.objects.get(id=id))

    return redirect(request.META.get('HTTP_REFERER'))


def edit_task(request, id):
    if request.method == "POST":
        edit_task_form = AddTaskForm(request.POST or None, instance=Task.objects.get(id=id))
        if edit_task_form.is_valid():
            edit = edit_task_form.save(commit=False)
            edit.project = Task.objects.get(id=id).project
            edit.save()
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        edit_task_form = AddTaskForm(instance=Task.objects.get(id=id))

    return redirect(request.META.get('HTTP_REFERER'))
