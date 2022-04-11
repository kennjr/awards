from django.forms import ModelForm, TextInput, Textarea

from awardsapp.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # when we use all as the val for the fields' var, then we tell django that we want a form that has input fields
        #  for all the columns that we've got in the table
        fields = ('name', 'description', 'tags', 'screenshot_1', 'screenshot_2', 'screenshot_3')
        widgets = {
            'name': TextInput(attrs={
                'class': "m_input",
                'placeholder': 'Project name'
                }),
            'description': Textarea(attrs={
                'class': "m_txt_area",
                'placeholder': 'Description'
                }),
            'tags': Textarea(attrs={
                'class': "m_txt_area",
                'placeholder': 'Tags'
                }),
        }
