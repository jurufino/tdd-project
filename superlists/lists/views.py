from django.shortcuts import render, redirect
from lists.models import List, Item


def home_page(request):
    if request.method == 'POST':
        try:
            list_ = List.objects.create()
            Item.objects.create(
                text=request.POST.get('item_text'),
                list=list_
            )
            return redirect(f'/lists/{list_.id}/')

        except Exception:
            return render(request, 'home.html', {
                'error': "Você não pode enviar um item vazio"
            })

    return render(request, 'home.html')


def new_list(request):
    try:
        list_ = List.objects.create()
        Item.objects.create(
            text=request.POST.get('item_text'),
            list=list_
        )
        return redirect(f'/lists/{list_.id}/')

    except Exception:
        return render(request, 'home.html', {
            'error': "Você não pode enviar um item vazio"
        })


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            Item.objects.create(
                text=request.POST.get('item_text'),
                list=list_
            )
            return redirect(f'/lists/{list_.id}/')

        except Exception:
            error = "Você não pode enviar um item vazio"

    items = Item.objects.filter(list=list_)

    return render(request, 'list.html', {
        'list': list_,
        'items': items,
        'error': error
    })