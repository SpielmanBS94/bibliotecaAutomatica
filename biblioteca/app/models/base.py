from django.db import models
from django.forms import ModelForm

class Base(models.Model):
    pass
class BaseForm(ModelForm):
    class Meta:
        model = Base
        fields = '__all__'
        exclude = []