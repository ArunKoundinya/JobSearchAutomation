from django import forms

class AcceptInputForm(forms.Form):
    CHOICES = [
        ('Indeed', 'Indeed'),
        ('GlassDoor', 'GlassDoor'),
        ('Naukri', 'Naukri')
    ]
    
    platform = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect
    )
    
    jobsearch = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter job search term'})
    )
    
    location = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter location'})
    )
    
    pages = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter number of pages'})
    )
