from django.urls import path
from . import views

# ====================================================

app_name = 'InternalVote'
urlpatterns = [
    ## index
    path('', views.index, name='index'),
    ## result
    path('result', views.result, name='result'),
]

