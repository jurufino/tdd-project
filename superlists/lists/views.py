from django.http import HttpResponse

items = []

def home_page(request):
    return HttpResponse('''
        <html>
            <title>To-Do lists</title>
            <body>
                <h1>Welcome to To-Do App</h1>
                <a href="/lists/">Go to your list</a>
            </body>
        </html>
    ''')


def view_list(request, list_id):
    item = request.GET.get('item_text')

    if item:
        items.append(item)

    list_html = ''
    for i, item in enumerate(items, start=1):
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