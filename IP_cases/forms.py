from django import forms
from IP_cases.models import district_courts_and_judges as judge

class indexform(forms.Form):
    Judges = forms.ModelChoiceField(queryset=judge.objects.all(), empty_label="--Select--")