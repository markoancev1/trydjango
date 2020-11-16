from django import forms

from .models import Singer


class SingerForm(forms.ModelForm):
    class Meta:
        model = Singer
        fields = [
            'first_name',
            'last_name',
            'group',
            'group_name',
            'from_macedonia',
            'age'
        ]


# class RawSingerForm(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     group = forms.BooleanField()
#     group_name = forms.CharField()
#     from_macedonia = forms.BooleanField()
#     age = forms.IntegerField()
