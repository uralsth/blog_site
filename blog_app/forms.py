from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
