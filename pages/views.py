from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator
from . filters import RentFilter

# Create your views here.

def homeView(request):
    return render(request, 'pages/index.html')

def aboutView(request):
    return render(request, 'pages/about.html')

def contactView(request):
    socials = Social.objects.all()
    contact = Contact.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, subject=subject, message=message)

        contact.save()

        messages.success(request, 'Your request has been submitted thank you')
        return redirect('contact')
    context = {
        'contact': contact,
        'socials':socials
    }
    return render(request, 'pages/contact.html', context)

def furnitureView(request):
    socials = Social.objects.all()
    furn = Furniture.objects.all()
    paginator = Paginator(Furniture.objects.all(), 6)
    page = request.GET.get('page')
    furn_page = paginator.get_page(page)
    nums = "a" *furn_page.paginator.num_pages
    
    context = {
        'furn':furn,
        'nums':nums,
        'furn_page':furn_page,
        'socials':socials
    }
    return render(request, 'pages/furnitures.html', context)

def furnitureDetailView(request, pk):
    furn = Furniture.objects.get(id=pk)
    
    context = {
        'furn':furn,
    }
    return render(request, 'pages/furn_details.html', context)

def saleView(request):
    socials = Social.objects.all()
    sales = Sale.objects.all()
    loc = Location.objects.all()
    paginator = Paginator(Sale.objects.all(), 6)
    page = request.GET.get('page')
    sales_page = paginator.get_page(page)
    nums = "a" *sales_page.paginator.num_pages
    
    locFilter = RentFilter(request.GET, queryset=sales)
    sales = locFilter.qs
    
    context = {
        'sales':sales,
        'nums':nums,
        'sales_page':sales_page,
        'socials':socials,
        'loc':loc
    }
    return render(request, 'pages/house_sale.html', context)

def saleDetailView(request, pk):
    sales = Sale.objects.get(id=pk)
    
    context = {
        'sales':sales,
    }
    return render(request, 'pages/sale_details.html', context)

def rentView(request):
    socials = Social.objects.all()
    rents = Rent.objects.all()
    states = State.objects.all()
    loc = Location.objects.all()
    bed = Bedroom.objects.all()
    bath = Bathroom.objects.all()
    garages = Garage.objects.all()
   
    
    locFilter = RentFilter(request.GET, queryset=rents)
    rents = locFilter.qs
    paginator = Paginator(rents, 6)
    page = request.GET.get('page')
    rent_page = paginator.get_page(page)
    nums = "a" *rent_page.paginator.num_pages
    
            
    context = {
        'rents':rents,
        'rent_page':rent_page,
        'nums':nums,
        'states':states,
        'loc':loc,
        'bed':bed,
        'bath':bath,
        'garages':garages,
        'locFilter':locFilter,
        'socials':socials
    }
    return render(request, 'pages/house_rent.html', context)

def rentDetailView(request, pk):
    rents = Rent.objects.get(id=pk)
    
    context = {
        'rents':rents,
    }
    return render(request, 'pages/rent_details.html', context)