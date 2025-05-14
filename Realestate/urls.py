from django.urls import path
from Realestate.views import home_view, listings_view, search, listing_detail, blog_view, logout_view

urlpatterns = [
    path('', home_view, name='home'),
    path('listings/', listings_view, name='listings'),
    path('search/', search, name='search'),
    path('listing/<int:id>/', listing_detail, name='listing_detail'),
    path('blog/', blog_view, name='blog'),
    path('logout', logout_view, name='logout'),
]