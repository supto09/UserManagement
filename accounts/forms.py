# accounts.forms.py
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User, Profile


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-lg no-b',
                'placeholder': 'Your Email',
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg no-b',
                'placeholder': 'Your Password'
            }
        ))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if not user:
                raise forms.ValidationError('Invalid email & password combination')

        super(LoginForm, self).clean()


class RegisterForm(forms.ModelForm):
    """
    Form for registering user
    """
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-lg no-b',
                'placeholder': 'Your Email',
            }
        ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-lg no-b',
            'placeholder': 'Your Password'
        }
    ))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-lg no-b',
            'placeholder': 'Confirm Password'
        }
    ))

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def clean(self):
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is already taken")

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.active = True  # Later we will add email verification
        if commit:
            user.save()
        return user


class RegisterWithProfile(RegisterForm):
    """
    Extended registration form that will also create user profile
    """
    firstName = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg no-b',
                'placeholder': 'Your First Name',
            }
        ))

    lastName = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg no-b',
                'placeholder': 'Your last Name',
            }
        ))

    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'email', 'password', 'password2')

    def save(self, **kwargs):
        user_instance = super().save(commit=True)

        first_name = self.cleaned_data['firstName']
        last_name = self.cleaned_data['lastName']

        profile = Profile(user=user_instance, firstName=first_name, lastName=last_name)
        profile.save()
        return user_instance


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user


class ProfileWithUserAdminCreationForm(UserAdminCreationForm):
    """
    Extended form for user creation that will contain profile and user information
    """
    firstName = forms.CharField(label='First Name', widget=forms.TextInput)
    lastName = forms.CharField(label='Last Name', widget=forms.TextInput)

    def save(self, commit=True):
        instance = super().save(commit=True)
        first_name = self.cleaned_data['firstName']
        last_name = self.cleaned_data['lastName']
        profile = Profile(
            user=instance,
            firstName=first_name,
            lastName=last_name
        )
        profile.save()
        return instance


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
