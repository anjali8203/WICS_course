from django import forms
from .models import UploadedFile, Message, Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'due_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Enter the project title',
            'class': 'form-control',
            'style': 'margin-bottom: 1rem;'
        })
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Provide a detailed description of the project',
            'class': 'form-control',
            'style': 'margin-bottom: 1rem;'
        })
        if 'due_date' in self.fields:
            self.fields['due_date'].widget.attrs.update({
                 'placeholder': 'Add the start date of your travel',
                'class': 'form-control',
                'type': 'date',  # Ensure this is a date input
                'style': 'margin-bottom: 1rem;'
            })

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file', 'title', 'description', 'keywords']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholders and Bootstrap classes to fields
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Enter a title for your project',
            'class': 'form-control',
            'style': 'margin-bottom: 1rem;'
        })
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Provide a brief description of the project',
            'class': 'form-control',
            'style': 'margin-bottom: 1rem;'
        })
        self.fields['keywords'].widget.attrs.update({
            'placeholder': 'Add keywords to help the project be quickly identified, separated by commas',
            'class': 'form-control',
            'style': 'margin-bottom: 1rem;'
        })
        self.fields['file'].widget.attrs.update({
            'class': 'form-control-file',
            'style': 'margin-bottom: 1rem;'
        })
        # Optional: Remove required attribute from fields
        self.fields['title'].required = False
        self.fields['description'].required = False
        self.fields['keywords'].required = False

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Write your message here...',
            'class': 'form-control',
            'style': 'margin-bottom: 1rem;'
        })

class AddMemberForm(forms.Form):
    user_id = forms.IntegerField(
        widget=forms.HiddenInput()
    )
