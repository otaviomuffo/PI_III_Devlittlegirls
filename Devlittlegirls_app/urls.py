from .views import site_list
from django.urls import path, re_path
#from Devlittlegirls_app.views import AlunoList , SiteList

app_name = 'Devlittlegirls_app'

urlpatterns = [
    path('', site_list, name='AlunoList_teste'),
]