from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm
from django.urls import reverse
def index(request):
    advertisements = Advertisement.objects.all()
    cntext = {"advertisements": advertisements}
    return render(request, 'index.html', cntext)

def top_sellers(request):
    return render(request, 'top-sellers.html')


# ------

# def advertisement_post(request):
#     if request.method == "POST":
#         form = AdvertisementForm(request.POST, request.FILES)
#         if form.is_valid():
#             advertisement = Advertisement(**form.cleaned_data)
#             advertisement.user = request.user
#             advertisement.save()
#             url = reverse('advertisement_post')
#             return redirect(url)
#     else:
#         form = AdvertisementForm()
#     context = {'form': form}
#     return render(request, 'advertisement-post.html', context)

def advertisement_post(request): 
    if request.method == "POST": 
        form = AdvertisementForm(request.POST, request.FILES) 
        if form.is_valid(): 
            advertisement = form.save(commit=False) 
            advertisement.user = request.user 
            advertisement.save() 
            url = reverse('advertisement_post') 
            return redirect(url) 
    else: 
        form = AdvertisementForm() 
    context = {'form': form} 
    return render(request, 'advertisement-post.html', context)

# ------





def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def advertisement(request):
    return render(request, 'advertisement.html')







# def advertisement_post(request):
#     return render(request, 'advertisement-post.html')
 
