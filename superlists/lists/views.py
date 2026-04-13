
from django.http import HttpResponseRedirect
from django.http import HttpResponse


lists = {}

next_id = 1

def home_page(request):
    global next_id

    item = request.GET.get('item_text')

    if item:
        list_id = next_id
        next_id += 1

        lists[list_id] = [item]

        return HttpResponseRedirect(f'/lists/{list_id}/')

    return HttpResponse('''
        <html>
            <title>To-Do lists</title>
            <body>
                <h1>Welcome to To-Do App</h1>

                <form method="GET">
                    <input name="item_text" placeholder="Enter a to-do item" />
                </form>
            </body>
        </html>
    ''')

def view_list(request, list_id):
    item = request.GET.get('item_text')

    if list_id not in lists:
        lists[list_id] = []

    if item:
        lists[list_id].append(item)

    list_html = ''
    for i, item in enumerate(lists[list_id], start=1):
        list_html += f'<tr><td>{i}: {item}</td></tr>'

    return HttpResponse(f'''
        <html>
            <title>To-Do lists</title>
            <body>
                <h1>List {list_id}</h1>

                <form method="GET">
                    <input name="item_text" placeholder="Enter a to-do item" />
                </form>

                <table>
                    {list_html}
                </table>
            </body>
        </html>
    ''')