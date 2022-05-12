from django import forms
from .models import Rooms

class RoomsForm(forms.ModelForm) :
    class Meta :
        model = Rooms
        fields = ('title', 'contents', )
