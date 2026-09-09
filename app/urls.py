from django.urls import path
from app.views import URLView

urlpatterns =[
    path('urls', URLView.as_view(), name='url-list-create')
]