from django import forms
from .models import students

class StudentsForm(forms.Form):

    name=forms.CharField(max_length=20,label='Name')
    track = forms.CharField(max_length=20, label='Track')
    class Meta:
        model = students
        fields = '__all__'


class StudentsForm_mode(forms.ModelForm):

    # name=forms.CharField(max_length=20, label='Name')
    # track=forms.CharField(max_length=20, label='Track')

    class Meta:
        model = students
        fields = '__all__'
