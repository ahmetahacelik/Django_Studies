from django.forms import ModelForm
from Lab.models import BlockPost

class ContactForm(ModelForm):
    class Meta:
        model=BlockPost

        fields = ['Title', 'Body']
