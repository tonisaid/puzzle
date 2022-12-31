from django import forms
from .models import UserInputs
class UserInputForm(forms.ModelForm):
    class Meta:
        model = UserInputs
        fields = "__all__"

        