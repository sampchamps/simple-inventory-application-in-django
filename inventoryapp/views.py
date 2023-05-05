from django.shortcuts import render

from .models import Item

# Create your views here.


def item_home(request):
    homes = Item.objects.all()
    return render(request, "inventory_templates/item_home.html", {homes: "homes"})


def item_list(request):
    items = Item.objects.all()
    return render(request, "inventory_templates/item_list.html", {items: "items"})


def item_form(request):
    return render(request, "inventory_template/item_form.html", {})


def item_bulk_upload(request):
    return render(request, "inventory_templates/item_bulk_upload.html", {})
