from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from clothing.models import Item


@login_required()
def profileView(request):
    return render(request, 'profile.html')
