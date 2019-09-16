from django.urls import path
from . import views

# ====================================================

app_name = 'InternalVote'
urlpatterns = [
    # /InternalVote/
    path('', views.index, name='index'),
    # /InternalVote/result
    path('result', views.result, name='result'),
    # /InternalVote/voted
    path('voted', views.voted, name='voted'),
]

