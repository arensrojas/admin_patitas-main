from django.shortcuts import render
from .models import Provider, Customer

# Create your views here.
def v_index(request):
    context = {
        "n_providers": 0,
        "n_customers": 0,
    }
    
    context["n_providers"] = Provider.objects.all().count()
    context["n_customers"] = Customer.objects.all().count()
    
    return render(request, 'administration/index.html', context)
    
    
def v_providers(request):
    context = {
        "providers_list" : Provider.objects.all()
    }
    return render(request, 'administration/providers.html', context)

def v_customers(request):
    context = {
        "customers_list" : Customer.objects.all()
    }
    return render(request, 'administration/customers.html', context)