from django.shortcuts import render, redirect
from lists.models import List, Item


def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)

    if request.method == 'POST':
        item_text = request.POST.get('item_text')

        if not item_text:
            items = Item.objects.filter(list=list_)
            return render(request, 'list.html', {
                'list': list_,
                'items': items,
                'error': "You can't have an empty list item"
            })

        Item.objects.create(
            text=item_text,
            list=list_
        )

        return redirect(f'/lists/{list_id}/')

    items = Item.objects.filter(list=list_)

    return render(request, 'list.html', {
        'list': list_,
        'items': items
    })


def new_list(request):
    list_ = List.objects.create()

    item_text = request.POST.get('item_text')

    if item_text:
        Item.objects.create(
            text=item_text,
            list=list_
        )

    return redirect(f'/lists/{list_.id}/')