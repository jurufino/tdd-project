from django.shortcuts import render, redirect
from lists.models import List, Item


def home_page(request):
    return render(request, 'home.html')


def new_list(request):
    list_ = List.objects.create()
    item_text = request.GET.get('item_text')

    if item_text:
        Item.objects.create(text=item_text, list=list_)

    return redirect(f'/lists/{list_.id}/')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)

    item_text = request.GET.get('item_text')
    if item_text:
        Item.objects.create(text=item_text, list=list_)

    items = Item.objects.filter(list=list_)

    return render(request, 'list.html', {
        'list': list_,
        'items': items
    })