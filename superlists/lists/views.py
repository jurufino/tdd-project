from django.http import HttpResponse
from django.shortcuts import redirect
from lists.models import List, Item


def home_page(request):
    return HttpResponse('''
        <h1>Welcome to To-Do App</h1>
        <form action="/lists/new" method="GET">
            <input name="item_text" placeholder="Enter a to-do item" />
        </form>
    ''')


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

    list_html = ''
    for i, item in enumerate(items, start=1):
        list_html += f'<tr><td>{i}: {item.text}</td></tr>'

    return HttpResponse(f'''
        <html>
            <title>To-Do lists</title>
        </html>
        <body>
            <h1>List {list_id}</h1>

            <form method="GET">
                <input name="item_text" placeholder="Enter a to-do item" />
            </form>

            <table>
                {list_html}
            </table>
        </body>
    ''')