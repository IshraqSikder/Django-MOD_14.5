from django import forms
from django.forms.widgets import NumberInput

class ExampleForm(forms.Form):
    name = forms.CharField(initial='Your name')
    email = forms.EmailField(label="Enter your email address")
    age = forms.IntegerField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    date = forms.DateField()
    
    # to apply this must import NumberInput
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    
    BIRTH_YEAR_CHOICES = ['2000', '2001', '2002']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    
    value = forms.DecimalField(label="Any decimel value")
    
    message = forms.CharField(max_length = 10)
    
    agree = forms.BooleanField(initial=True, label="Are you sure to submit")