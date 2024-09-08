from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

def health(request):
    try:
        user = get_user_model().objects.get(id=2)
    except User.DoesNotExist:
        user = None
    return HttpResponse(user)