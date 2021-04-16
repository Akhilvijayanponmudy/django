from django import forms


class StudentRegistrationForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'box'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'box'}))
    course=forms.CharField(max_length=120)
    phone=forms.CharField(max_length=12)
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=120)

    def clean(self):
        print("inside clean")



