from django import forms

from accounts.models import User
from doctor_website.models import Service


class AddServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddServiceForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Title"
        self.fields['caption'].label = "Caption"
        self.fields['image_icon'].label = "logo"

        self.fields['caption'].widget.attrs.update(
            {
                'placeholder': 'Enter a caption',
            }
        )
        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'Enter a title',
            }
        )

    class Meta:
        model = Service
        fields = ['title', 'caption', 'image_icon']

    def is_valid(self):
        valid = super(AddServiceForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        service = super(AddServiceForm, self).save(commit=False)
        if commit:
            service.save()
        return service


class ActiveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ActiveForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['role'].label = "Role"
        self.fields['email'].label = "Email"
        self.fields['phone_number'].label = "Phone Number"
        self.fields['is_active'].label = "Active account"
        self.fields['first_name'].widget.attrs.update(
            {

                'readonly': 'readonly'

            }
        )
        self.fields['last_name'].widget.attrs.update(
            {

                'readonly': 'readonly'

            }
        )
        self.fields['role'].widget.attrs.update(
            {

                'readonly': 'readonly'

            }
        )
        self.fields['email'].widget.attrs.update(
            {

                'readonly': 'readonly'

            }
        )
        self.fields['phone_number'].widget.attrs.update(
            {

                'readonly': 'readonly'

            }
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'role', 'email', 'phone_number', 'is_active']

    def is_valid(self):
        valid = super(ActiveForm, self).is_valid()
        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        user = super(ActiveForm, self).save(commit=False)
        if commit:
            user.save()
        return user
