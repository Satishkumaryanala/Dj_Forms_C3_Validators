from django import forms

def check_for_a(value):
    if value[0].lower() in 'a':
        raise forms.ValidationError('Name starts with A')

def check_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('Length is less then 5')


class StudentForm(forms.Form):
    Sname = forms.CharField(max_length=100,validators=[check_for_a,check_for_len])
    Sid = forms.IntegerField()
    Sage = forms.IntegerField()
    Semail = forms.EmailField( validators=[check_for_a,check_for_len])

