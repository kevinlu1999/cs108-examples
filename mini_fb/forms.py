from django import forms
from .models import Profile, StatusMessage

BIRTH_YEAR_CHOICES = [i for i in range(1992, 2013)]


class CreateProfileForm(forms.ModelForm):
    '''A form to create a new profile object'''
    first_name = forms.CharField(label='first_name', required=True)
    last_name = forms.CharField(label='last_name', required=True)
    birth_date = forms.DateField(label='birth_date', required=True, widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    city = forms.CharField(label='city', required=True)
    email_address = forms.CharField(label='email', required=True)
    profile_image_url = forms.URLField(label='image_url', required=True)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'city', 'email_address', 'profile_image_url']


class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='first_name', required=True)
    last_name = forms.CharField(label='last_name', required=True)
    birth_date = forms.DateField(label='birth_date', required=True, widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    city = forms.CharField(label='city', required=True)
    email_address = forms.CharField(label='email', required=True)
    profile_image_url = forms.URLField(label='image_url', required=True)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'city', 'email_address', 'profile_image_url']


class CreateStatusMessageForm(forms.ModelForm):
    image = forms.ImageField(label='image', required=False)

    class Meta:
        model = StatusMessage
        fields = ['message', 'image']
