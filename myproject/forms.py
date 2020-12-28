from django.forms import ModelForm
from myapp.models import Contact
from django.forms import modelformset_factory


class OrderForm(ModelForm):
	class Meta:
		model = Contact
		fields = ['name', 'description', 'moderator','category']


