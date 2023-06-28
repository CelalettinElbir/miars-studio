from django import forms
from .models import project_photo, message


# class ProjectPhotosForm(forms.ModelForm):
#     image = forms.ImageField(
#         widget=forms.ClearableFileInput(attrs={'multiple': True}))

#     class Meta:
#         model = project_photo
#         fields = ('image', 'is_default')


