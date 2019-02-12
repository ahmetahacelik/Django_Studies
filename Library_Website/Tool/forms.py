from django import forms
class ToolForm(forms.Form):
    text=forms.CharField(widget=forms.Textarea)