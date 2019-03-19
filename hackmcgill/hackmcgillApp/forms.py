from django import forms

from .models import HackAdmin, Person, User

# when a User is saved, a corresponding HackAdmin is made at the same time - and the two are connected by a 1-1 relationship
# the username of the User is the email ; Thus, HackAdmin form is only the Role.
class UserForm (forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True,
                             help_text=' --> must be a valid address')
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta():
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email already exists.")
        return email

    def save(self, *args, **kwargs):
        data = self.cleaned_data
        user = User(username=data['email'], email=data['email'], first_name=data['first_name'],
                    last_name=data['last_name'], password=data['password'], )
        user.set_password(data['password'])
        user.admin_profile = None
        user.save()
        return user

class HackAdminForm (forms.ModelForm):
    class Meta():
        model = HackAdmin
        fields = [
            'Role',
        ]

class PersonForm (forms.ModelForm):
    class Meta():
        model = Person
        fields = [
            'First_name',
            'Last_name',
            'Email',
        ]