from django import forms

from accounts.models import Profile


class ProfileUpdateForm(forms.ModelForm):
    """
    Form for updating user profile
    """
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )

    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    bio = forms.CharField(
        label='Bio',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    birth_date = forms.DateField(
        label='Birth Date',
        required=False,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'class': 'date-time-picker form-control form-control-lg',
                'data-options': '{"theme":"light","timepicker":false,"format":"Y-m-d"}'
            }
        ))
    hobby = forms.CharField(
        label='Hobby',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name:
            print('first name validatetion', first_name)
            raise forms.ValidationError('First Name is required')

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if not last_name:
            print('last_name validatetion', last_name)
            raise forms.ValidationError('Last Name is required')

        return last_name

    def save(self, commit=True):
        profile = super(ProfileUpdateForm, self).save(commit=False)
        if commit:
            profile.save()
        return profile
