#import autocomplete_light
import selectable.forms as selectable
from django.forms.models import modelformset_factory
from rango.lookups import UserProfileLookup
#autocomplete_light.autodiscover()
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import HiddenInput
from rango.models import Category, Page, UserProfile, WorkExperience, Education
import datetime
from image_cropping import ImageCropWidget

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name:")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page:")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page:")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')
    
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
    
        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('password', 'email')

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['firstName'].label = "First Name"
        self.fields['lastName'].label = "Last Name"
        self.fields['linkedIn'].label = "LinkedIn (Optional)"
    class Meta:
        model = UserProfile
        

class UserRegistrationForm(forms.ModelForm):
    
    class meta:
        model = User

class WorkExperienceForm(forms.ModelForm):
    company = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class':'special-input'}))
    jobTitle = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class':'special-input'}))
    location = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class':'special-input'}))
    info = forms.CharField(max_length=1000, widget= forms.Textarea(attrs={'class':'special-input info-input'}))
    
    class Meta:
        model = WorkExperience

class EducationForm(forms.ModelForm):
    
    class Meta:
        model = Education

class AddGroupForm(forms.Form):
    user = forms.CharField(
        label='Type the name of a classmate',
        widget=selectable.AutoComboboxSelectWidget(UserProfileLookup,  allow_new=True),
        required=False,
    )
