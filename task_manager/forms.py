from django import forms

from task_model_manager.models import Note, Project, Task


class UpdateNoteForm(forms.ModelForm):
    is_done = forms.BooleanField(label="", widget=forms.CheckboxInput(
        attrs={"class": "is_done_with_note", "required": False}), required=False)

    class Meta:
        model = Note
        fields = ('is_done',)


class AddProjectForm(forms.ModelForm):
    project = forms.CharField(label="", widget=forms.Textarea(
        attrs={"class": "form-control col", "placeholder": "Project name...", "rows": "3"}))

    start_date = forms.DateField(label="", widget=forms.DateInput(
        attrs={"type": "date", "class": "form-control form-control-sm border-0 px-0"}))
    end_date = forms.DateField(label="", widget=forms.DateInput(
        attrs={"type": "date", "class": "form-control form-control-sm border-0 px-0"}))

    class Meta:
        model = Project
        fields = ('project', 'start_date', 'end_date')


class AddTaskForm(forms.ModelForm):

    task = forms.CharField(label="", widget=forms.Textarea(
        attrs={"class": "form-control col", "placeholder": "Task name...", "rows": "3"}))
    start_date = forms.DateField(label="", widget=forms.DateInput(
        attrs={"type": "date", "class": "form-control form-control-sm border-0 px-0"}))
    end_date = forms.DateField(label="", widget=forms.DateInput(
        attrs={"type": "date", "class": "form-control form-control-sm border-0 px-0"}))
    project = forms.Select(
        attrs={"class": "form-select", "required": False})

    class Meta:
        model = Task
        fields = ('task', 'start_date', 'end_date', 'project')


class AddNoteForm(forms.ModelForm):

    note = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "form-control col border-0", "placeholder": "Add Note..."}))
    task = forms.Select(
        attrs={"required": False})

    class Meta:
        model = Note
        fields = ('note', 'task')


class AddNoteForm2(forms.ModelForm):

    note = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "form-control col border-0", "placeholder": "Add Note..."}))

    class Meta:
        model = Note
        fields = ('note',)
