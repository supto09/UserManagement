from django import forms

from accounts.models import Profile


class ProfileUpdateForm(forms.ModelForm):
    """
    Form for updating user profile
    """
    firstName = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )

    )
    lastName = forms.CharField(
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
    birthDate = forms.DateField(
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
        fields = ('firstName', 'lastName', 'bio', 'birthDate', 'hobby')

    def clean_firstName(self):
        first_name = self.cleaned_data.get("firstName")
        if not first_name:
            print('first name validatetion', first_name)
            raise forms.ValidationError('First Name is required')

        return first_name

    def clean_lastName(self):
        last_name = self.cleaned_data.get("lastName")
        if not last_name:
            print('last_name validatetion', last_name)
            raise forms.ValidationError('Last Name is required')

        return last_name

    def save(self, commit=True):
        profile = super(ProfileUpdateForm, self).save(commit=False)
        if commit:
            profile.save()
        return profile
