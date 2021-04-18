from django.forms import ModelForm
from mobile.models import Brands,Mobile

class BrandCreateForm(ModelForm):
    class Meta:
        model=Brands
        fields="__all__"


class MobileCreateForm(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"
