from django.shortcuts import redirect, render
from Realestate.models import Listing, Slides, advert, founder, Blog
from .forms import SearchForm
from django.contrib.auth import logout

def home_view(request):
    slides = Slides.objects.all()
    latest_listings = Listing.objects.order_by('-posted_at')[:6]
    ad = advert.objects.all()
    founders = founder.objects.all()
    form = {
        'slides': slides,
        'latest_listings': latest_listings,
        'ad': ad,
        'founders': founders,
    }
    return render(request, 'index.html', form,)


def listings_view(request):
    listings = Listing.objects.all()
    return render(request, 'listings.html', {'listings': listings})


def search(request):
    form = SearchForm(request.GET)
    listings = Listing.objects.all()

    if form.is_valid():
        print(form.cleaned_data)
        if form.cleaned_data['price']:
            listings = listings.filter(price__lte=form.cleaned_data['price'])
        if form.cleaned_data['city']:
            listings = listings.filter(city__iexact=form.cleaned_data['city'].upper())
        if form.cleaned_data['category']:
            listings = listings.filter(category__iexact=form.cleaned_data['category'].upper())
        # if form.cleaned_data['bedrooms_num']:
        #     listings = listings.filter(bedrooms_num=form.cleaned_data['bedrooms_num'])
        # if form.cleaned_data['bathrooms_num']:
        #     listings = listings.filter(bathrooms_num=form.cleaned_data['bathrooms_num'])
        # if form.cleaned_data['garage_num']:
        #     listings = listings.filter(garage_num=form.cleaned_data['garage_num'])
        # if form.cleaned_data['area_size']:
        #     listings = listings.filter(area_size=form.cleaned_data['area_size'])
        print(listings.query)
    return render(request, 'listings.html', {'listings': listings})


def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, 'listing_detail.html', {'listing': listing})


def blog_view(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

def logout_view(request):
    logout(request)
    return redirect('home')


