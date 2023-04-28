from django.shortcuts import render

from .models import Item

# Create your views here.


def item_list(request):
    return render(request, "inventory_templates/item_list.html", {})
