from django import forms

class StationForm(forms.Form):
        CHOICES = (('a','Not Ready'),
                   ('b','Need Help'),
                   ('c','Ready'),)
        picked = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())

        def get_choices(self):
                print [val for val in CHOICES]
                return "HI"
