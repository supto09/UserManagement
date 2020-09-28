from accounts import forms
from accounts.models import Profile


class RegisterForm(forms.ModelForm):
    """
    Form for updating user profile
    """

    # email = forms.EmailField(
    #     widget=forms.EmailInput(
    #         attrs={
    #             'class': 'form-control form-control-lg no-b',
    #             'placeholder': 'Your Email',
    #         }
    #     ))
    # password = forms.CharField(widget=forms.PasswordInput(
    #     attrs={
    #         'class': 'form-control form-control-lg no-b',
    #         'placeholder': 'Your Password'
    #     }
    # ))
    # password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
    #     attrs={
    #         'class': 'form-control form-control-lg no-b',
    #         'placeholder': 'Confirm Password'
    #     }
    # ))
    #
    class Meta:
        model = Profile
        # fields = ('email', 'password', 'password2')
    #
    # def clean(self):
    #     email = self.cleaned_data.get('email')
    #     password1 = self.cleaned_data.get("password")
    #     password2 = self.cleaned_data.get("password2")
    #
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords don't match")
    #
    #     qs = User.objects.filter(email=email)
    #     if qs.exists():
    #         raise forms.ValidationError("Email is already taken")
    #
    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super(RegisterForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data["password"])
    #     user.active = True  # Later we will add email verification
    #     if commit:
    #         user.save()
    #     return user
