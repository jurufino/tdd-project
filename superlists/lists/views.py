from django.http import HttpResponse

def home_page(request):
    return HttpResponse('''
        <html>
            <title>To-Do lists</title>
            <body>
                <input placeholder="Enter a to-do item" />
            </body>
        </html>
    ''')