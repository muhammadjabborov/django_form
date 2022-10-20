from django.forms import ModelForm

from app.models import Employer


class EmployerModelForm(ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'
