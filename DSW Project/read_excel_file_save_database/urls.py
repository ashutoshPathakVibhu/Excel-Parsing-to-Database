from django.urls import path
from . import views

app_name = "read_excel_file_save_database"

urlpatterns = [
    path('',views.index,name='index'),
]