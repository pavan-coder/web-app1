import django.forms as forms

from .models import Room


class Tenant_RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        
        
class 