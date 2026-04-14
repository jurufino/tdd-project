from django.shortcuts import render, redirect
from lists.models import List, Item


def home_page(request):
    if request.method == 'POST':
        if request.POST.get('item_text') == '':
            return render(request, 'home.html', {
                'error': "Você não pode enviar um item vazio"
            })

        list_ = List.objects.create()
        Item.objects.create(
            text=request.POST.get('item_text'),
            list=list_
        )
        return redirect(f'/lists/{list_.id}/')

    return render(request, 'home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)

    error = None

    if request.method == 'POST':
        if request.POST.get('item_text') == '':
            error = "Você não pode enviar um item vazio"
        else:
            Item.objects.create(
                text=request.POST.get('item_text'),
                list=list_
            )

    items = Item.objects.filter(list=list_)

    return render(request, 'list.html', {
        'list': list_,
        'items': items,
        'error': error
    })


def new_list(request):
    if request.POST.get('item_text') == '':
        return render(request, 'home.html', {
            'error': "Você não pode enviar um item vazio"
        })

    list_ = List.objects.create()
    Item.objects.create(
        text=request.POST.get('item_text'),
        list=list_
    )
    return redirect(f'/lists/{list_.id}/')