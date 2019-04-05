import datetime as dt
from .models import Record
from django import forms


HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(10, 20)]

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        exclude = ['id'] 
        widgets = {'time': forms.Select(choices=HOUR_CHOICES), 'date': forms.SelectDateWidget()}