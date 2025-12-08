from django.urls import path
from . import views

app_name = 'converter'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/encode/', views.encode_image, name='encode_image'),
    path('api/decode/', views.decode_image, name='decode_image'),
]
