from django.forms import ModelForm

from dummysignup.models import UserProfile


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['beach', 'nature', 'shopping', 'history', 'food']
