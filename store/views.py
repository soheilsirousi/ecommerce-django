from lib2to3.fixes.fix_input import context

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from store.models import Category, Product

def health(request):
    try:
        user = get_user_model().objects.get(id=2)
    except User.DoesNotExist:
        user = None
    return HttpResponse(user)


def index(request):
    return render(request, 'main/index.html')

class CategoryDetailView(View):
    template_name = 'store/category.html'

    def get(self, request, name, *args, **kwargs):
        data = Category.objects.filter(name=name)
        if data.exists():
            return render(request, self.template_name, {'data': data})
        return HttpResponse(content='not found', status=404)
