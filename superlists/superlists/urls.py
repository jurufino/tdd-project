from django.contrib import admin
from django.urls import path
from lists.views import home_page, view_list, new_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('lists/new', new_list),  # 🔥 ESSA LINHA
    path('lists/<int:list_id>/', view_list),
]