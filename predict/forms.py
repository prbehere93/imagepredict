from django import forms

class ImageForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )