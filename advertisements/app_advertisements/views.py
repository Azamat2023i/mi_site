from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement, User
from .forms import AdvertisementForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Count

def index(request):
    title = request.GET.get("query")
    # print(title)
    if title:
        advertisements = Advertisement.objects.filter(title__contains=title)
    else:
        advertisements = Advertisement.objects.all()
    # print(advertisements)
    # advertisements = Advertisement.objects.all()
    cntext = {
        "advertisements": advertisements,
        "title": title
        }
    return render(request, 'app_advertisments/index.html', cntext)


def top_sellers(request):
    users = User.objects.annotate(adv_count=Count('advertisement')).order_by('-adv_count')
    context = {'users': users}
    return render(request, 'app_advertisments/top-sellers.html', context)


def advertisement(request):
    return render(request, 'app_advertisments/advertisement.html')


@login_required(login_url=reverse_lazy('login'))
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
    return render(request, 'app_advertisments/advertisement-post.html', context)


def advertisments_datail(request, pk):
    advertisement = Advertisement.objects.get(id=pk)
    context = {"adv": advertisement}
    return render(request, 'app_advertisments/advertisement.html', context)