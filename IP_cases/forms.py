from django import forms
from IP_cases.models import district_courts_and_judges as judge
from IP_cases.models import notice_of_appearence as notice,location

locations_choice = ( 
              (loc.id, "%s,%s"%(loc.office, loc.state)) for loc in location.objects.all()
            )

class LocationForm(forms.Form):
    loc = forms.CharField(max_length=30,widget=forms.Select(choices=locations_choice))


class NoaForm(forms.ModelForm):
    class Meta:
	model = notice
	exclude = ('location',)




    
