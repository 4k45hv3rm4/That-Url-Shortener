from django import forms
from .validators import validate_url, validate_dot_com


class SubmitURLForm(forms.Form):
    url = forms.CharField(
            label = '',
            validators=[validate_url, validate_dot_com],
            widget = forms.TextInput(
                attrs = {
                    "placeholder" : " Type Your Long URL HERE...",
                    "class " :"form-control text-decoration-none",

                    }
                )
            )


    # def clean(self):
    #     cleaned_data = super(SubmitURLForm, self).clean()
    #     print(cleaned_data)
    #     url = self.cleaned_data.get('url')
    #     url_validator = URLValidator()
    #     try:
    #         # print("Validating")
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL for the Field")
    #     return url
    #     # url = cleaned_data['url']
    #     # print(url)

    # def clean_url(self):
    #     # pr/int("error")
    #     url = self.cleaned_data.get['url']
    #     # if not 'com' in url:
    #     #     raise forms.ValidationError("This is not valid because of No .com ")
        # return url

