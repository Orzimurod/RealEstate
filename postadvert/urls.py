from django.urls import path

from postadvert.views import postadvert_view

urlpatterns = [
    path('postadvert/', postadvert_view, name='postadvert')
]
