from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import PostadvertForm
from django.contrib import messages


@login_required(login_url='login')
def postadvert_view(request):
    if request.method == 'POST':
        form = PostadvertForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "E'loningiz yuborildi, admin tasdiqlagandan keyin ko'rinadi.")
            return redirect('home')
    else:
        form = PostadvertForm()
    return render(request, 'post_an_ad.html', {'form': form})


