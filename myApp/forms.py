from django import forms
#permite poder hacer que una clase se extienda con unas caracteristicas para que despues se convierta en un archivo html

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    description= forms.CharField(label="Descripcion de la tarea", widget= forms.Textarea(attrs={
        'class':'input'
    }), required=False)


class CreateNewProject(forms.Form):
    name=forms.CharField(label='Nombre', max_length=200, required=False, widget=forms.TextInput(attrs={
        'class':'input'
    }))