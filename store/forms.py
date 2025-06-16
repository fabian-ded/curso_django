from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'inputt'}))
    description = forms.CharField(label="Descripcion de la tarea", widget=forms.Textarea(attrs={'class': 'inputt'}))
    id_project = forms.IntegerField(label="Id del proyecto")
    
class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombra tu brillante idea", max_length=100, widget=forms.TextInput(attrs={'class': 'inputt'}))