"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.shortcuts import render, redirect 
from myapp.models import Contact 
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect 
from .forms import OrderForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

from django.forms import ModelForm
from myapp.models import Contact

from django.forms import ModelForm
from myapp.models import Contact
from django.forms import modelformset_factory



class OrderForm(ModelForm):
	class Meta:
		model = Contact
		fields = ['name', 'description','category']

def Main(request):
    
    return render(request, 'main.html')
    



def loginPage(request):
	if request.user.is_authenticated:
		return redirect('updateOrder')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('updateOrder')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)


def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'model_form.html', context)

@login_required(login_url='login')
def updateOrder(request):
    ProductFormSet = modelformset_factory(Contact, fields=('name', 'description', 'moderator','category',),)
    data = request.POST or None
    formset = ProductFormSet(data=data, queryset=Contact.objects.filter(moderator=''))
    for form in formset:
        form.fields['moderator'].queryset = Contact.objects.filter(moderator='')

    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return redirect('/')

    return render(request, 'formset.html', {'formset': formset})
    

def list_view_cheminfo(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    context["dataset"] = Contact.objects.filter(moderator='Yes', category='Cheminformatics') 
          
    return render(request, "list_view.html", context) 

def list_view_compchem(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    context["dataset"] = Contact.objects.filter(moderator='Yes', category='CompChem') 
          
    return render(request, "list_view.html", context) 

def list_view_bioinfo(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    context["dataset"] = Contact.objects.filter(moderator='Yes', category='Bioinformatics') 
          
    return render(request, "list_view.html", context) 

def list_view_compbio(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    context["dataset"] = Contact.objects.filter(moderator='Yes', category='CompBio') 
          
    return render(request, "list_view.html", context) 

def list_view_tut(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    context["dataset"] = Contact.objects.filter(moderator='Yes', category='Tutorials') 
          
    return render(request, "list_view.html", context) 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main, name='Main'),
    path('loginPage/', loginPage, name='loginPage'),
    path('createOrder/', createOrder, name='createOrder'),
    path('updateOrder/', updateOrder, name='updateOrder'),
    path('list_view_cheminfo/', list_view_cheminfo, name='list_view_cheminfo'),
    path('list_view_compchem/', list_view_compchem, name='list_view_compchem'),
    path('list_view_bioinfo/', list_view_bioinfo, name='list_view_bioinfo'),
    path('list_view_compbio/', list_view_compbio, name='list_view_compbio'),
    path('list_view_tut/', list_view_tut, name='list_view_tut'),

    
]
